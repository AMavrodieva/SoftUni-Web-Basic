# Generated by Django 4.1.2 on 2022-10-25 16:01

import django.core.validators
from django.db import migrations, models
import my_music_app.music.validators


class Migration(migrations.Migration):

    dependencies = [
        ("music", "0001_initial"),
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
                (
                    "username",
                    models.CharField(
                        max_length=15,
                        validators=[
                            django.core.validators.MinLengthValidator(2),
                            my_music_app.music.validators.validate_only_alphanumeric,
                        ],
                    ),
                ),
                ("email", models.EmailField(max_length=254)),
                ("age", models.PositiveIntegerField(blank=True, null=True)),
            ],
        ),
    ]


