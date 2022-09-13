from datetime import datetime
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    user_title = models.CharField(max_length = 50)
    user_body = models.TextField()
    user_date_created = models.DateTimeField(default = timezone.now)
    user_owner = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self) -> str:
        return f'Owner - {self.user_owner}, Post - {self.user_title}'