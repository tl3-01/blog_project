# Generated by Django 4.2.3 on 2023-07-13 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='BlogPost',
        ),
    ]