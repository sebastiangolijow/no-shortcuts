from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from taggit.managers import TaggableManager

from core_apps.common.models import TimeStampedModel
from .read_time_engine import ArticleReadTimeEngine

User = get_user_model()


class Article(TimeStampedModel):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="articles")
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    slug = AutoSlugField(populate_from="title", always_update=True, unique=True)
    description = models.CharField(max_length=255, verbose_name=_("description"))
    body = models.TextField(verbose_name=_("article content"))
    banner_image = models.ImageField(
        verbose_name=_("banner image"), default="/profile_default.png"
    )
    tags = TaggableManager()

    def __str__(self):
        return self.title

    @property
    def time_estimated_reading_time(self):
        return ArticleReadTimeEngine.estimate_reading_time(self)

    def view_count(self):
        return self.article_views.count()


class ArticleView(TimeStampedModel):
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name="article_views"
    )
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, related_name="user_views", null=True
    )
    viewer_ip = models.GenericIPAddressField(
        verbose_name=_("viewer ip"), null=True, blank=True
    )

    class Meta:
        verbose_name = _("Article view")
        verbose_name_plural = _("Article views")
        unique_together = ("article", "user", "viewer_ip")

    def __str__(self):
        username = self.user.first_name if self.user else ""
        return f"{self.article.title} viewed by {username}"

    @classmethod
    def record_view(cls, article, user, viewed_ip):
        view, _ = cls.objects.get_or_create(
            article=article, user=user, viewed_ip=viewed_ip
        )
        view.save()
