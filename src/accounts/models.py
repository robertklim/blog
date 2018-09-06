from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user    = models.OneToOneField(User, on_delete=models.CASCADE)
    image   = models.ImageField(default='profile_default.jpg', upload_to='profile_images')

    def __str__(self):
        return f'{self.user.username} Profile'