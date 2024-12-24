from django.db import models
from django.contrib.auth.models import AbstractUser



# Create your models here.


class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatars', null=True, blank=True)
    job = models.CharField(max_length=50, null=True, blank=True)
    bio = models.TextField(max_length=120, null=True, blank=True)


    # def save(self, *args, **kwargs):
    #     if self.pk is None or not self.password.startswith('pbkdf2_sha256$'):
    #         self.set_password(self.password)
    #     super(User, self).save(*args, **kwargs)

