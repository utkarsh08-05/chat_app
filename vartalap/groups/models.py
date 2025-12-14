from django.db import models
from django.contrib.auth.models import User

class Groups(models.Model):
    name=models.CharField(max_length=100)
    created_by=models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='created_groups'
    )
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
class GroupMember(models.Model):
    group=models.ForeignKey(
        Groups,
        on_delete=models.CASCADE,
        related_name='members'
    )
    user=models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='group_membership'
    )
    joined_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together=('group','user')
        verbose_name = "Group"
        verbose_name_plural = "Groups"
    def __str__(self):
        return f"{self.user} is in {self.group}"



