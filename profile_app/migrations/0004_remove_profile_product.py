# Generated by Django 4.2.1 on 2023-06-20 23:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profile_app', '0003_alter_profile_date_joined'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='product',
        ),
    ]
