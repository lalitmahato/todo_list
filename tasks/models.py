from typing import Any
from django.db import models
from users.models import CustomUser


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(CustomUser, related_name='creator', on_delete=models.SET_NULL, null=True, blank=True)
    modifier = models.ForeignKey(CustomUser, related_name='modifier', on_delete=models.SET_NULL, null=True, blank=True)
    assign_to = models.ForeignKey(CustomUser, related_name='assign_to', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title

