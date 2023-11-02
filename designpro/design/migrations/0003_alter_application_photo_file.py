# Generated by Django 4.2.7 on 2023-11-02 12:42

import design.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('design', '0002_category_application'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='photo_file',
            field=models.ImageField(blank=True, default='default.jpg', upload_to=design.models.get_name_file),
        ),
    ]
