# Generated by Django 4.1 on 2024-04-22 08:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="OurPosts",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=20, verbose_name="タイトル")),
                ("date", models.DateTimeField(auto_now_add=True, verbose_name="日付")),
                (
                    "photo1",
                    models.ImageField(
                        blank=True, upload_to="images/", verbose_name="写真"
                    ),
                ),
                ("content", models.TextField(max_length=700, verbose_name="コンテンツ")),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("notice", "お知らせ"),
                            ("foods", "グルメ"),
                            ("bestspot", "ベストスポット"),
                            ("events", "イベント"),
                            ("news", "ニュース"),
                            ("others", "その他"),
                        ],
                        max_length=15,
                        verbose_name="カテゴリー",
                    ),
                ),
                (
                    "valid_for_public",
                    models.CharField(
                        choices=[("公開", "公開"), ("非公開", "非公開")],
                        default="非公開",
                        max_length=15,
                        verbose_name="全体公開許可",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        default="noname",
                        on_delete=django.db.models.deletion.SET_DEFAULT,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "post",
            },
        ),
    ]
