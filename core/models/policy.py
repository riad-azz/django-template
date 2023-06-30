from utils.model import Model, TitleSlugModel
from ckeditor.fields import RichTextField
from django_extensions.db.models import ActivatorModel, TimeStampedModel
from django.urls import reverse


class Policy(ActivatorModel, TimeStampedModel, TitleSlugModel, Model):
    body = RichTextField()

    class Meta:
        verbose_name_plural = "Policies"

    def get_absolute_url(self):
        return reverse('core:policy_detail', kwargs={'slug': self.slug})
