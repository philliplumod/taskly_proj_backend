from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from.models import Profile

"""
Signal handler to create a user profile when a new User instance is created.

This function listens to the `post_save` signal of the `User` model. When a new
user is created (`created` is True), it automatically creates a corresponding
`Profile` instance linked to the user.

"""

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)