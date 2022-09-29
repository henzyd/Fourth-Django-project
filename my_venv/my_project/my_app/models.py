from django.utils import timezone
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    user_title = models.CharField(max_length = 50)
    user_body = models.TextField()
    user_date_created = models.DateTimeField(default = timezone.now)
    user_owner = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self) -> str:
        return f'Owner - {self.user_owner}, Post - {self.user_title}, {self.id}'

    def get_absolute_url(self): ##### NOTE this is like redirect
        return reverse('plist_detail_page', kwargs={'pk': self.id})


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(default='profile/default.jpg', upload_to='profile-pics/')