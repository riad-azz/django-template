from utils.model import Model
from ckeditor.fields import RichTextField
from django_extensions.db.models import ActivatorModel, TimeStampedModel, TitleSlugDescriptionModel


class Event(ActivatorModel, TimeStampedModel, TitleSlugDescriptionModel, Model):
    body = RichTextField()

    class Meta:
        verbose_name_plural = "Our Events"
