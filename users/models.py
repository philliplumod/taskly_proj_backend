from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils.deconstruct import deconstructible

import os
import uuid


class CustomUser(AbstractUser):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.username


@deconstructible
class GenerateProfileImagePath(object):
    def __call__(self, instance, filename):
        ext = filename.split(".")[1]
        path = f"media/accounts/{instance.user.user_id}/images/"
        name = f"profile_image.{ext}"
        return os.path.join(path, name)


user_profile_image_path = GenerateProfileImagePath()


class Profile(models.Model):
    profile_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=user_profile_image_path, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
