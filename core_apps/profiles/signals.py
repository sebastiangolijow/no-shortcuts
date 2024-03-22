import logging

from django.db.models.signals import post_save
from django.dispatch import receiver
from authots_api.settings.base import AUTH_USER_MODEL
from .models import Profile

logger = logging.getLogger(__name__)


@receiver(post_save, sender=AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        logger.info("Profile has been created")
