# Generated by Django 3.1.4 on 2021-01-08 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210102_0755'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='hobby',
            field=models.CharField(default='nothing', max_length=30),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='normal',
            field=models.CharField(default='No', max_length=30),
        ),
    ]
