# Generated by Django 4.2 on 2023-12-23 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("network", "0005_remove_follower_followed_users_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="like",
            field=models.IntegerField(default=0),
        ),
    ]
