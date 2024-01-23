# Generated by Django 4.2 on 2023-12-19 01:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("network", "0004_follower"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="follower",
            name="followed_users",
        ),
        migrations.RemoveField(
            model_name="follower",
            name="followers",
        ),
        migrations.RemoveField(
            model_name="follower",
            name="user",
        ),
        migrations.AddField(
            model_name="follower",
            name="followed",
            field=models.ForeignKey(
                default="",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="followed",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="follower",
            name="follower",
            field=models.ForeignKey(
                default="",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="follows",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.CreateModel(
            name="Like",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "post",
                    models.ForeignKey(
                        default="",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="post_liked",
                        to="network.post",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        default="",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_liked",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]