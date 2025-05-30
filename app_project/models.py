from django.db import models

# Create your models here.

class Omonim(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    

class Details(models.Model):
    name = models.ForeignKey(Omonim, on_delete=models.CASCADE)
    kelib_chiqishi = models.CharField(max_length=100, null=True)
    absolutus = models.CharField(max_length=250)
    soz_turkimi = models.CharField(100)
    manosi = models.TextField()
    misollar = models.TextField()


    def __str__(self):
        return self.manosi
