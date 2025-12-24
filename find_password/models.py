from django.db import models
from django.core.exceptions import ValidationError

from . import validators

class Account(models.Model):
    old_password = models.CharField(max_length=255)
    new_password = models.CharField(max_length=255)
    confirm_new_password = models.CharField(max_length=255)