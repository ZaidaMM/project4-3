# Generated by Django 4.2.2 on 2024-02-03 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("network", "0009_remove_user_followers"),
    ]

    operations = [
        migrations.RenameField(
            model_name="post",
            old_name="user",
            new_name="author",
        ),
    ]
