from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
  class Meta:
    verbose_name = 'Post'
    verbose_name_plural = 'Posts'

  title = models.CharField(max_length=200)
  description = models.CharField(max_length=400, default='', blank=True)
  content = models.TextField()
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  favicon = models.ImageField(upload_to='posts/favicon', default=None, blank=True)

  def __str__(self):
    return self.title