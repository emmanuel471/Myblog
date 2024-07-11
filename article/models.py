from django.db import models

class Topic(models.Model):
    topic_name = models.CharField(max_length=100)

    def __str__(self):
        return self.topic_name

class Article(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='articles')
    title = models.CharField(max_length=200)
    article = models.TextField()
    image = models.ImageField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title