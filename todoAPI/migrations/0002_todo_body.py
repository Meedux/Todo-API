# Generated by Django 5.0.6 on 2024-05-16 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todoAPI", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="todo",
            name="body",
            field=models.TextField(default=""),
            preserve_default=False,
        ),
    ]
