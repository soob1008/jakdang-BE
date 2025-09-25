from django.db import models

class Page(models.Model):
    id = models.UUIDField(primary_key=True)
    user_id = models.UUIDField()
    slug = models.SlugField(unique=True)
    theme_id = models.IntegerField(null=True, blank=True)
    style_draft = models.JSONField(null=True, blank=True)
    style_published = models.JSONField(null=True, blank=True)
    block_draft = models.JSONField(null=True, blank=True)
    block_published = models.JSONField(null=True, blank=True)
    title = models.CharField(max_length=255)

    class Meta:
        db_table = "pages"
        managed = False   # Supabase에 이미 있는 테이블이라면 꼭 필요