from django.db import models

from django.contrib.auth.models import User
class Message(models.Model):
    sender=models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='sent_message'

    )
    receiver=models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recieved_message'
    )
    content=models.TextField(blank=True,null=True)
    media_file=models.FileField(
        upload_to='chat_media/',
        blank=True,
        null=True
    )
    mediaType=models.CharField(max_length=10,
                                      choices=[
                                          ('text','Text'),
                                          ('image','Image'),
                                          ('video','Video'),
                                          ('file','File')
                                      ],
                                      default='text'
                                      
                                      )
    timestamp=models.DateTimeField(auto_now_add=True)
    is_seen=models.BooleanField(default=False)
    def __str__(self):
        return f"{self.sender}---> {self.receiver}"