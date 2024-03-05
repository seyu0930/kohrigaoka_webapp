from django import forms
from .models import OurPosts
from PIL import Image
from django.core.exceptions import ValidationError

class OurPostForm(forms.ModelForm):
    class Meta:
        model = OurPosts
        fields = ( "title", "content", "photo1", "category")
        
        exclude = ["valid_for_public"]