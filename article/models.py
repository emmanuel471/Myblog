from django.db import models

# Create your models here.

class Topic(models.Model):
    topic_name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.topic_name
    
class Article(models.Model):
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE,related_name='article')
    title = models.CharField(max_length=200)
    article = models.TextField()
    image = models.ImageField()
    created_date = models.DateTimeField(auto_now_add=True)
