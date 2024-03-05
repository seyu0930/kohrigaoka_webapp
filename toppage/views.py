from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import TemplateView, View
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from .models import OurPosts
from .forms import OurPostForm
from django.shortcuts import redirect
from django.contrib import messages
from PIL import Image
from django.core.exceptions import ValidationError
# Create your views here.
#-------------------------------------------------
class ToppageView(ListView):
    template_name = "toppage/base.html"
    model = OurPosts
    paginate_by = 10

    def get_queryset(self):
        return OurPosts.objects.order_by('-date', "-id")

top = ToppageView.as_view()

#-------------------------------------------------
class MypageView(LoginRequiredMixin, ListView):
    template_name = "toppage/mypage.html"
    model = OurPosts
    paginate_by = 10

    def get_queryset(self):
        return OurPosts.objects.order_by('-date',"-id")

mypage = MypageView.as_view()

#-------------------------------------------------
class CreatePostView(LoginRequiredMixin, CreateView):
    model = OurPosts
    form_class = OurPostForm
    ordering = "-date"
    template_name = "toppage/createpost.html"
    success_url = reverse_lazy("toppage:mypage")
    def post(self, request, *args,**kwargs):
        if request.method == 'POST':
            form = OurPostForm(request.POST)
            if form.is_valid():
                if request.POST.get("photo1") != "":
                    form = form.save(commit=False)
                    form.valid_for_public = "非公開"
                    form.user = request.user
                    form.photo1 = request.FILES["photo1"]
                    image = Image.open(form.photo1)
                    if image.width * image.height > 4000*4000:
                        messages.error(request, "投稿に失敗しました。画像のサイズが大きすぎます")
                        return redirect('toppage:createpost')
                    form.save()
                    return redirect('toppage:mypage')
                messages.error(request, "投稿に失敗しました。画像の投稿を忘れていませんか？")
                return redirect('toppage:createpost')

            
createpost = CreatePostView.as_view()

#-------------------------------------------------
class DetailPostView(DetailView):
    model = OurPosts
    template_name = "toppage/postdetail.html"

    

postdetail = DetailPostView.as_view()

#-------------------------------------------------

class DeletePostView(LoginRequiredMixin, DeleteView):
    model = OurPosts
    template_name = "toppage/deletepost.html"
    success_url = reverse_lazy("toppage:mypage")

deletepost = DeletePostView.as_view()

#-------------------------------------------------

class CategoryView(ListView):
    model = OurPosts
    template_name = 'toppage/category.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = OurPosts.objects.order_by('-id').filter(category=self.kwargs['category'])
        return queryset

category = CategoryView.as_view()


#-------------------------------------------------

class UserPageView(ListView):
    model = OurPosts
    template_name = 'toppage/userpages.html'
    paginate_by = 10
    

    def get_queryset(self):
        queryset = OurPosts.objects.order_by('-id').filter(user_id=self.kwargs['user_id'])
        return queryset
    

user = UserPageView.as_view()

class ManagementView(UserPassesTestMixin, ListView):
    model = OurPosts
    template_name = 'toppage/management.html'
    paginate_by = 10
        
    def test_func(self):
        # スーパーユーザーでなければ４０３ページ
        return self.request.user.is_superuser
    
    def get_queryset(self):
            queryset = OurPosts.objects.order_by('-id').filter(valid_for_public=self.kwargs['valid_for_public'])
            return queryset
    

management = ManagementView.as_view()

#-------------------------------------------------
def Approve(request, pk):
    current_model = OurPosts.objects.get(pk=pk)
    current_model.valid_for_public = "公開"
    current_model.save()
    return redirect("/management/非公開/")

def Inapprove(request, pk):
    current_model = OurPosts.objects.get(pk=pk)
    current_model.valid_for_public = "非公開"
    current_model.save()
    return redirect("/management/公開/")

#-------------------------------------------------