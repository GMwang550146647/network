# Generated by Django 3.1.4 on 2021-01-13 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20210113_1256'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Author_Book',
            new_name='Book_Author',
        ),
    ]
