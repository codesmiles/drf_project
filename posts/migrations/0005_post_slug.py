# Generated by Django 5.0.6 on 2024-06-10 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0004_rename_posts_post"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="slug",
            field=models.CharField(max_length=20, null=True),
        ),
    ]
