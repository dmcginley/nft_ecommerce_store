from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image


# from store_app.models import Product


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)

    image = models.ImageField(
        default='default.jpg', upload_to='profile_pics')
    date_joined = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} Profile'
