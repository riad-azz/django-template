import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_extensions.db.fields import AutoSlugField


class Model(models.Model):
    id = models.UUIDField(
        _("id"),
        primary_key=True,
        default=uuid.uuid4
    )

    class Meta:
        abstract = True


class TitleSlugModel(models.Model):
    slug = AutoSlugField(_('slug'), populate_from='title', overwrite=True)
    title = models.CharField(_('title'), max_length=255)

    class Meta:
        abstract = True
