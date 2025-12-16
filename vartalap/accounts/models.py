from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    bio=models.TextField(blank=True)
    created=models.DateTimeField(auto_now_add=True)
    profileimage=models.ImageField(
        upload_to='profiles/',
        blank=True,
        null=True
    )
    last_seen=models.DateTimeField(default=now)
    def __str__(self):
        return self.user.username



