# Generated by Django 4.1.2 on 2022-10-30 08:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("car_app", "0001_initial"),
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
                        max_length=10,
                        validators=[
                            django.core.validators.MinLengthValidator(
                                2, "The username must be a minimum of 2 chars"
                            )
                        ],
                    ),
                ),
                ("email", models.EmailField(max_length=254)),
                (
                    "age",
                    models.IntegerField(
                        validators=[django.core.validators.MinValueValidator(18)]
                    ),
                ),
                ("password", models.CharField(max_length=30)),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=30, null=True, verbose_name="First Name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=30, null=True, verbose_name="Last Name"
                    ),
                ),
                (
                    "profile_picture",
                    models.URLField(
                        blank=True, null=True, verbose_name="Profile Picture"
                    ),
                ),
            ],
        ),
    ]