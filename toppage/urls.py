from django.urls import path

from . import views

app_name = 'toppage'
urlpatterns = [
    path('', views.top, name="top"),
    path('mypage/',views.mypage, name="mypage"),
    path('createpost/',views.createpost, name="createpost"),
    path('postdetail/<int:pk>/',views.postdetail,name='postdetail'),
    #path('editpost/',views.editpost, name="editpost"),
    path('deletepost/<int:pk>/',views.deletepost, name="deletepost"),
    path('category/<str:category>/', views.category,name='category'),
    path('userpages/<int:user_id>/', views.user,name='user'),
    path('management/<str:valid_for_public>/', views.management,name='management'),
    path('approve/<int:pk>', views.Approve, name='approve'),
    path('inapprove/<int:pk>', views.Inapprove, name='inapprove'),
]