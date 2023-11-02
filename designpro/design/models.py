from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=255)

    groups = models.ManyToManyField(
        Group,
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name="customuser_set",
        related_query_name="user",
    )

    user_permissions = models.ManyToManyField(
        Permission,
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="customuser_set",
        related_query_name="user",
    )

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)

class DesignRequest(models.Model):
    STATUS_CHOICES = [
        ('N', 'Новая'),
        ('P', 'Принято в работу'),
        ('C', 'Выполнено'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='designs/')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='N')
    timestamp = models.DateTimeField(auto_now_add=True)