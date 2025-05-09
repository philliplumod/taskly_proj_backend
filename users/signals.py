from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from.models import Profile

"""
Signal handler to create a user profile when a new User instance is created.

This function listens to the `post_save` signal of the `User` model. When a new
user is created (`created` is True), it automatically creates a corresponding
`Profile` instance linked to the user.

Args:
    sender (Model): The model class that sent the signal (in this case, `User`).
    instance (User): The instance of the `User` model that was saved.
    created (bool): A boolean indicating whether a new record was created.
    **kwargs: Additional keyword arguments passed by the signal.
"""

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)