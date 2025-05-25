from django.db import models
from django.contrib.auth.models import User
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify
import os

# Create your models here.
class Port(models.Model):
  time = models.IntegerField(default=0)
  title = models.CharField(max_length=50, unique=True)
  content = MarkdownxField()
  thumb1 = models.ImageField(upload_to='single_pages/images/%Y/%m/%d/', blank=True)
  thumb2 = models.ImageField(upload_to='single_pages/images/%Y/%m/%d/', blank=True)
  
  def __str__(self):
    return f'{self.title}'

  def get_content_markdown(self):
    return markdownify(self.content)

class Page(models.Model):
  name = models.CharField(max_length=20)
  html = models.FileField(upload_to='single_pages/images/%Y/%m/%d/')
  
  def __str__(self):
    return f'{self.name} - {self.html.url}'
