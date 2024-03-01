from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    pass
    #account_id = models.SlugField(verbose_name="アカウントID", max_length=18),
    #password = models.SlugField(verbose_name="アカウントID", max_length=18),