# Generated by Django 3.2.10 on 2022-06-26 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0008_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='img',
            field=models.FileField(max_length=64, upload_to='city/', verbose_name='图片'),
        ),
    ]