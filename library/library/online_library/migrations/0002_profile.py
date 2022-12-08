# Generated by Django 4.1.2 on 2022-10-27 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("online_library", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Profile",
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
                ("first_name", models.CharField(max_length=30)),
                ("last_name", models.CharField(max_length=30)),
                ("image_url", models.URLField()),
            ],
        ),
    ]
