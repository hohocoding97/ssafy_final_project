# Generated by Django 4.2.13 on 2024-05-20 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_user_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='nick_name',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
