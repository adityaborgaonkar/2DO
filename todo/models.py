from django.db import models
import datetime

class TodoItem(models.Model):
    content = models.CharField(max_length=100)

class BookItem(models.Model):
    content = models.CharField(max_length=100)
    
class MusicItem(models.Model):
    content = models.CharField(max_length=100)

class CourseItem(models.Model):
    content = models.CharField(max_length=100)

class BingeItem(models.Model):
    content = models.CharField(max_length=100)


