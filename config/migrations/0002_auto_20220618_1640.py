# Generated by Django 3.2.10 on 2022-06-18 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='create_time',
            field=models.DateField(verbose_name='入职时间'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='depart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='config.department', verbose_name='部门'),
        ),
    ]