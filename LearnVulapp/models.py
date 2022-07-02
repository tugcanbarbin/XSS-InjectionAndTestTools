from django.db import models
from django.urls import reverse


# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length =1000)
    

class Comment(models.Model):
    book = models.ForeignKey(Book,related_name="comments", on_delete=models.CASCADE)
    nickname = models.CharField(max_length=200)
    body = models.TextField()
    def get_absolute_url(self):
        return reverse("feed")
    

    def __str__(self):
        return '%s-%s' %(self.book.title,self.nickname)
    