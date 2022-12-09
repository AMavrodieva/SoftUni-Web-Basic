from django.core import exceptions
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models
from django.utils.deconstruct import deconstructible


def validator_only_letters(value):
    if not value.isalpha():
        raise ValidationError('Ensure this value contains only letters.')


def validator_max_size_image(value):
    if value.file.size > 5 * 1024 * 1024:
        raise ValidationError('Max file size is 5 MB')

# @deconstructible
# class MaxSizeInMbValidator:
#     def __int__(self, max_size=None):
#         self.max_size = max_size
#
#     def __call__(self, value):
#         if self.max_size is not None and value.size > (self.max_size * 1024 * 1024):
#             raise ValidationError(f'Max file size is {self.max_size:.2f} MB')



class Profile(models.Model):
    FIRST_NAME_MIN_LEN = 2
    FIRST_NAME_MAX_LEN = 15

    LAST_NAME_MIN_LEN = 2
    LAST_NAME_MAX_LEN = 15

    BUDGET_DEFAULT_VALUE = 0
    BUDGET_MIN_VALUE = 0

    IMAGE_MAX_SIZE = 5
    IMAGE_UPLOAD_DIR = 'profiles/'

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LEN),
            validator_only_letters,
        ),
        null=False,
        blank=False,
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LEN,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LEN),
            validator_only_letters,
        ),
        null=False,
        blank=False,
    )

    budget = models.FloatField(
        default=BUDGET_DEFAULT_VALUE,
        validators=(
            MinValueValidator(BUDGET_MIN_VALUE),
        ),
        null=False,
        blank=False,
    )

    profile_image = models.ImageField(
        upload_to=IMAGE_UPLOAD_DIR,
        null=True,
        blank=True,
        validators=(
            validator_max_size_image,
            # MaxSizeInMBValidator(IMAGE_MAX_SIZE),
        ),
    )


class Expenses(models.Model):
    TITLE_MAX_LEN = 30

    title = models.CharField(
        max_length=TITLE_MAX_LEN,
        null=False,
        blank=False,
    )

    expense_image = models.URLField(
        null=False,
        blank=False,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    price = models.FloatField(
        null=False,
        blank=False,
    )
