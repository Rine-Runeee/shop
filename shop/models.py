from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=300)
    img = models.ImageField(upload_to='images/')
    text = models.TextField()
    price = models.PositiveBigIntegerField()
    added_at = models.DateTimeField(auto_now_add=True) #i speack english vary much
    rating = models.PositiveIntegerField()
    discount = models.PositiveSmallIntegerField(default=0)
    stock = models.PositiveIntegerField()
    manufacturer = models.TextField()
