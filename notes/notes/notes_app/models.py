from django.db import models


class Profile(models.Model):
    FIRST_NAME_MAX_LEN = 20
    LAST_NAME_MAX_LEN = 20

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN,
        null=False,
        blank=False,
        verbose_name='First Name'
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LEN,
        null=False,
        blank=False,
        verbose_name='Last Name',
    )

    age = models.PositiveIntegerField(
        null=False,
        blank=False,

    )

    image_url = models.URLField(
        null=False,
        blank=False,
        verbose_name='Link to Profile Image'
    )


class Note(models.Model):
    TITLE_MAX_LEN = 30

    title = models.CharField(
        max_length=TITLE_MAX_LEN,
        null=False,
        blank=False,
    )

    image_url = models.URLField(
        null=False,
        blank=False,
        verbose_name='Link to Image',
    )

    content = models.TextField(
        null=False,
        blank=False,
    )

    class Meta:
        ordering = ('pk',)
