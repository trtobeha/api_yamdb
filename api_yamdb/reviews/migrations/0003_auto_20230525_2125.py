# Generated by Django 3.2 on 2023-05-25 16:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('reviews', '0002_auto_20230524_2029'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='confirmation_code',
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(
                choices=[
                    ('admin', 'Administrator'),
                    ('moderator', 'Moderator'),
                    ('user', 'User'),
                ],
                default='user',
                max_length=10,
            ),
        ),
    ]
