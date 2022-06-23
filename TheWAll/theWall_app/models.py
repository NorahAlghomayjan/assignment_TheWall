from email import message
from django.db import models
import re
import bcrypt
from datetime import datetime
import time
from login_register_app.models import User
# Create your models here.


class Message (models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User,related_name='messages',on_delete=models.CASCADE)
    

class Comment (models.Model):
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User,related_name='comments',on_delete=models.CASCADE)
    message = models.ForeignKey(Message,related_name='comments',on_delete=models.CASCADE)
    