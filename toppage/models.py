from django.db import models
from django.utils import timezone
from accounts.models import CustomUser
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class OurPosts(models.Model):
    class Meta:
        db_table = "post"

    categories_select = (
        ("notice", "お知らせ"),
        ("foods", "グルメ"),
        ("bestspot", "ベストスポット"),
        ("events", "イベント"),
        ("news", "ニュース"),
        ("others", "その他"),

    )

    valid_select = (
        ("公開", "公開"),
        ( "非公開", "非公開"),
    )
    
    user = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default="noname")
    title = models.CharField(verbose_name="タイトル", max_length=20)
    date = models.DateTimeField(verbose_name="日付", auto_now_add=True)
    photo1 = models.ImageField(verbose_name="写真", upload_to="images/",blank=True)
    content = models.TextField(verbose_name="コンテンツ", max_length=700)
    category = models.CharField(verbose_name="カテゴリー", max_length=15,choices=categories_select)
    valid_for_public = models.CharField(verbose_name="全体公開許可", max_length=15, choices=valid_select, default="非公開")

    def __str__(self):
        return self.title