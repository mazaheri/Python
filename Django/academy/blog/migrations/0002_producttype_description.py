# Generated by Django 3.2 on 2023-07-17 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producttype',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
