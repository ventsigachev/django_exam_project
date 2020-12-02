from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Story(models.Model):
    title = models.CharField(max_length=70)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
