from django.db import models
import uuid

# Create your models here.
class Page(models.Model):
    id = models.UUIDField()
    user_id = models.UUIDField()

    slug = models.CharField(max_length=50)
    title = models.CharField(max_length=200)

    theme_id = models.CharField(max_length=50, blank=True, null=True)

    # JSONB 필드
    style_draft = models.JSONField(default=dict, blank=True)        # 초안 스타일
    style_published = models.JSONField(default=dict, blank=True)    # 발행 스타일
    block_draft = models.JSONField(default=list, blank=True)        # 블록 초안
    block_published = models.JSONField(default=list, blank=True)    # 블록 발행본

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.slug})"