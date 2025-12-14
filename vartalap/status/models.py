from django.db import models
from django.contrib.auth.models import User

class Status(models.Model):
    user=models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='statususer'
    )
    media_file=models.FileField(upload_to='status_media/')
    captions=models.TextField(blank=True)
    created_on=models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = "Status"
        verbose_name_plural = "Statuses"
    def __str__(self):
        return f"{self.user} uploaded this status"