from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models


class Profile(models.Model):
    USERNAME_MAX_LEN = 10
    USERNAME_MIN_LEN = 2
    ERROR_MESSAGE = "The username must be a minimum of 2 chars"

    AGE_MIN_VALUE = 18

    PASSWORD_MAX_VALUE = 30

    FIRST_NAME_MAX_LEN = 30
    LAST_NAME_MAX_LEN = 30

    username = models.CharField(
        max_length=USERNAME_MAX_LEN,
        validators=(MinLengthValidator(USERNAME_MIN_LEN, ERROR_MESSAGE),),
        null=False,
        blank=False,
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.IntegerField(
        null=False,
        blank=False,
        validators=(MinValueValidator(AGE_MIN_VALUE),),
    )

    password = models.CharField(
        max_length=PASSWORD_MAX_VALUE,
        null=False,
        blank=False,
    )

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN,
        null=True,
        blank=True,
        verbose_name='First Name',
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LEN,
        null=True,
        blank=True,
        verbose_name='Last Name',
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
        verbose_name='Profile Picture',
    )


class Car(models.Model):
    TYPE_MAX_LEN = 10
    CHOICES = (
        ("Sports Car", "Sports Car"),
        ("Pickup", "Pickup"),
        ("Crossover", "Crossover"),
        ("Minibus", "Minibus"),
        ("Other", "Other"),
    )

    MODEL_MIN_LEN = 2
    MODEL_MAX_LEN = 20

    YEAR_MIN_VALUE = 1980
    YEAR_MAX_VALUE = 2049
    ERROR_MESSAGE = 'Year must be between 1980 and 2049'

    PRICE_MIN_VALUE= 1

    type = models.CharField(
        max_length=TYPE_MAX_LEN,
        choices=CHOICES,
        null=False,
        blank=False,
    )

    model = models.CharField(
        max_length=MODEL_MAX_LEN,
        validators=(MinLengthValidator(MODEL_MIN_LEN),),
        null=False,
        blank=False,
    )

    year = models.IntegerField(
        validators=(
            MinValueValidator(YEAR_MIN_VALUE, ERROR_MESSAGE),
            MaxValueValidator(YEAR_MAX_VALUE, ERROR_MESSAGE),
        ),
        null=False,
        blank=False,
    )

    image_url = models.URLField(
        null=False,
        blank=False,
        verbose_name="Image URL"
    )

    price = models.FloatField(
        validators=(MinValueValidator(PRICE_MIN_VALUE), ),
        null=False,
        blank=False,
    )

    class Meta:
        ordering = ('pk',)

