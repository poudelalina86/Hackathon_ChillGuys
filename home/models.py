from django.db import models
from django.utils import timezone 
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.urls import reverse 

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class PostComment(models.Model):
    sno = models.AutoField(primary_key = True)
    comments = models.TextField()
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    post = models.ForeignKey(Post, on_delete= models.CASCADE)
    # parent = models.ForeignKey('self', on_delete= models.CASCADE, null=True, related_name='parents')
    timestamp = models.DateTimeField(default=now )