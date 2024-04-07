from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    name = models.CharField(max_length=100)

class Quote(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    text = models.TextField()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)