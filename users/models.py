from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class UserProfile(models.Model):
    first_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=20, blank=True)
    info = models.TextField(blank=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    location = models.CharField(max_length=20, blank=True)
    picture = models.ImageField(default='default_pic.jpg', upload_to='profile_pics')
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"User {self.user.username} Profile"

# Using Django Signals to create automatically user profile when user is created


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
