import os
from os.path import basename

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from PIL import Image

class Profile(models.Model):
    user    = models.OneToOneField(User, on_delete=models.CASCADE)
    image   = models.ImageField(default='default_profile.jpg', upload_to='profile_images')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        old_profile_image = Profile.objects.get(pk=self.pk).image
        if (basename(old_profile_image.name) != basename(self.image.name) and basename(old_profile_image.name) != Profile._meta.get_field('image').default):
            os.remove(os.path.join(settings.MEDIA_ROOT, old_profile_image.name))

        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
