from django.db import models
from utils.model import Model, TitleSlugModel
from django_extensions.db.models import ActivatorModel, TimeStampedModel


class Contact(ActivatorModel, TimeStampedModel, TitleSlugModel, Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    message = models.TextField(max_length=1000)

    class Meta:
        verbose_name_plural = "Contacts via website"
