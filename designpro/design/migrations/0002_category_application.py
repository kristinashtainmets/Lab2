# Generated by Django 4.2.7 on 2023-11-02 11:34

import design.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('design', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(help_text='Enter a brief description of the application', max_length=1000)),
                ('photo_file', models.ImageField(blank=True, max_length=254, null=True, upload_to=design.models.get_name_file, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])])),
                ('status', models.CharField(choices=[('N', 'Новая'), ('P', 'Принято в работу'), ('C', 'Выполнено')], default='N', max_length=254, verbose_name='Статус')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('category', models.ManyToManyField(help_text='Select a genre for this application', to='design.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='design.customuser', verbose_name='Пользователь')),
            ],
        ),
    ]
