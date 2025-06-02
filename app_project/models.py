from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    

class Term(models.Model):
    word = models.CharField(max_length=100)
    definition = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


    def __str__(self):
        return self.word
