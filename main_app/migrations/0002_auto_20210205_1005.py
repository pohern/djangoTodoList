# Generated by Django 3.1.6 on 2021-02-05 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='list',
            old_name='lisst',
            new_name='body',
        ),
    ]