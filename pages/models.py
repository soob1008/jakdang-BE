from django.db import models
import uuid

class Page(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.UUIDField()
    slug = models.SlugField(unique=True)
    theme_id = models.IntegerField(null=True, blank=True)
    style_draft = models.JSONField(null=True, blank=True)
    style_published = models.JSONField(null=True, blank=True)
    block_draft = models.JSONField(null=True, blank=True)
    block_published = models.JSONField(null=True, blank=True)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title