# Generated by Django 3.1.6 on 2021-02-08 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_auto_20210206_1019'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rating',
            old_name='comments',
            new_name='items',
        ),
    ]
