# Generated by Django 3.2 on 2023-07-27 22:00

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0003_auto_20230718_0838'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='product',
            managers=[
                ('default_manager', django.db.models.manager.Manager()),
            ],
        ),
    ]
