from django.db import models


class Profile(models.Model):
    FIRST_NAME_MAX_LEN = 30
    LAST_NAME_MAX_LEN = 30

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN,
        null=False,
        blank=False,
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LEN,
        null=False,
        blank=False,
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )


class Book(models.Model):
    TITLE_MAX_LEN = 30
    TYPE_MAX_LEN = 30

    title = models.CharField(
        max_length=TITLE_MAX_LEN,
        null=False,
        blank=False,
    )

    description = models.TextField(
        null=False,
        blank=False,
    )

    image = models.URLField(
        null=False,
        blank=False,
    )

    type = models.CharField(
        max_length=TYPE_MAX_LEN,
        null=False,
        blank=False,
    )
