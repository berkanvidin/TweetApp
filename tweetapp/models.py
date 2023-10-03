from typing import Any
from django.db import models
from django.contrib.auth.models import User

class Tweet(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    message = models.CharField(max_length=150)

    def __str__(self):
        return f"Tweet user:{self.username} message: {self.message}"
