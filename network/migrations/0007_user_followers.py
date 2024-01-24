# Generated by Django 4.2 on 2024-01-23 13:54

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("network", "0006_post_like"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="followers",
            field=models.ManyToManyField(
                blank=True, related_name="following", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]