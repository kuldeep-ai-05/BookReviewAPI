from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title=models.CharField(max_length=200)
    author=models.CharField(max_length=100)
    genre=models.CharField(max_length=50)
    published_year=models.IntegerField()

    def __str__(self):
        return self.title

class Review(models.Model):
    book=models.ForeignKey(Book,on_delete=models.CASCADE,related_name='reviews')
    reviewer=models.ForeignKey(User,on_delete=models.CASCADE,related_name='reviews')
    rating=models.IntegerField()
    text=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review of {self.book.title} by {self.reviewer.username}"
