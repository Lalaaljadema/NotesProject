from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username

class Note(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.CharField(max_length=100)
    no_of_likes = models.IntegerField(default=0)
    title = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class LikeNotes(models.Model):
    notes_id = models.CharField(max_length=100)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username