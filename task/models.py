from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class SocialMediaAccount(models.Model):
    PLATFORM_CHOICES = [
        ('Facebook', 'Facebook'),
        ('Twitter', 'Twitter'),
        ('Instagram', 'Instagram'),
        ('LinkedIn', 'LinkedIn'),
        ('Other', 'Other'),
    ]

    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    platform = models.CharField(max_length=100, choices=PLATFORM_CHOICES)
    username = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.platform}: {self.username}"
    
    def save(self, *args, **kwargs):
        # Automatically update username to match the User model username
        if self.user_profile and not self.username:
            self.username = self.user_profile.user.username
        super().save(*args, **kwargs)
