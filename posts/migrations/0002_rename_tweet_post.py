# Generated by Django 4.0 on 2022-05-04 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tweet',
            new_name='Post',
        ),
    ]