from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    class Meta:
        db_table = 'User'
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователя'

    image = models.ImageField(upload_to='users_images', verbose_name='Аватар', blank=True, null=True)

    def __str__(self):
        return self.username
