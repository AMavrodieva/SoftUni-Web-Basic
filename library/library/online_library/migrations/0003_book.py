# Generated by Django 4.1.2 on 2022-10-27 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("online_library", "0002_profile"),
    ]

    operations = [
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=30)),
                ("description", models.TextField()),
                ("image", models.URLField()),
                ("type", models.CharField(max_length=30)),
            ],
        ),
    ]