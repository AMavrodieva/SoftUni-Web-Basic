from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Profile(models.Model):
    AGE_MIN_VALUE = 12
    PASSWORD_MAX_LEN = 30
    FIRST_NAME_MAX_LEN = 30
    LAST_NAME_MAX_LEN = 30

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.IntegerField(
        null=False,
        blank=False,
        validators=(
            MinValueValidator(AGE_MIN_VALUE),
        ),
    )

    password = models.CharField(
        max_length=PASSWORD_MAX_LEN,
        null=False,
        blank=False,
    )

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN,
        null=True,
        blank=True,
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LEN,
        null=True,
        blank=True,
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )


class Game(models.Model):
    TITLE_MAX_LEN = 30
    CATEGORY_MAX_LEN = 15
    RATING_MIN_VALUE = 0.1
    RATING_MAX_VALUE = 5.0
    LEVEL_MIN_VALUE = 1
    ACTION = "Action"
    ADVENTURE = "Adventure"
    PUZZLE = "Puzzle"
    STRATEGY = "Strategy"
    SPORTS = "Sports"
    BOARD_CARD_GAME = "Board/Card Game"
    OTHER = "Other"

    CATEGORY = (
        (ACTION, ACTION),
        (ADVENTURE, ADVENTURE),
        (PUZZLE, PUZZLE),
        (STRATEGY, STRATEGY),
        (SPORTS, SPORTS),
        (BOARD_CARD_GAME, BOARD_CARD_GAME),
        (OTHER, OTHER),
    )

    title = models.CharField(
        max_length=TITLE_MAX_LEN,
        unique=True,
        null=False,
        blank=False,
    )

    category = models.CharField(
        max_length=CATEGORY_MAX_LEN,
        choices=CATEGORY,
        null=False,
        blank=False,
    )

    rating = models.FloatField(
        validators=(
            MinValueValidator(RATING_MIN_VALUE),
            MaxValueValidator(RATING_MAX_VALUE),
        ),
        null=False,
        blank=False,
    )

    max_level = models.IntegerField(
        null=True,
        blank=True,
        validators=(
            MinValueValidator(LEVEL_MIN_VALUE),
        ),
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    summary = models.TextField(
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ('pk',)
