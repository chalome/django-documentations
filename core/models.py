from django.db import models
from django.contrib.auth.models import AbstractUser

class Reporter(models.Model):
    full_name = models.CharField(max_length=70)
    email=models.EmailField(blank=True,null=True)
    
    
    def __str__(self):
        return self.full_name

class Article(models.Model):
    pub_date = models.DateField()
    headline = models.CharField(max_length=200)
    content = models.TextField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE,related_name='articles',related_query_name='article')
    
    def __str__(self):
        return self.headline

class CustomUser(AbstractUser):
    age = models.IntegerField(blank=True,null=True)
    address = models.CharField(max_length=100,blank=True,null=True)
    phone = models.CharField(max_length=15,blank=True,null=True)

class ProductQuerySet(models.QuerySet):
    def available(self):
        return self.filter(quantity__gt=0)
    
    def discount(self):
        return self.filter(discount__gt=0)
    def expensive(self):
        return self.filter(price__gt=1000)
    def cheap(self):
        return self.filter(price__lt=1000)
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True,null=True)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name='products',related_query_name='product')
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    discount = models.DecimalField(max_digits=10, decimal_places=2,blank=True,null=True)
    
    objects = ProductQuerySet.as_manager()
    
    def __str__(self):
        return self.name