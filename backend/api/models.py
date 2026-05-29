from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    address = models.TextField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    secondary_email = models.EmailField(blank=True)

    def __str__(self):
        return self.user.email

class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes", null=True)

    def __str__(self):
        return self.title
