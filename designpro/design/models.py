from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.crypto import get_random_string


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

    def __str__(self):
        return self.name


def get_name_file(instance, filename):
    return '/'.join([get_random_string(length=5) + '_' + filename])


class Application(models.Model):
    STATUS_CHOICES = [
        ('N', 'Новая'),
        ('P', 'Принято в работу'),
        ('C', 'Выполнено'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, help_text="Enter a brief description of the application")
    category = models.ManyToManyField(Category, help_text="Select a genre for this application")
    photo_file = models.ImageField(max_length=254, upload_to='image/',
                                   validators=[FileExtensionValidator(['jpg', 'jpeg', 'png', 'bmp'])])
    status = models.CharField(max_length=254, verbose_name='Статус', choices=STATUS_CHOICES, default='N')
    date = models.DateTimeField(verbose_name='Дата добавления', auto_now_add=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='requests')
