from django.db import models
from django.db.models import F, Sum
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class TagModel(models.Model):
    caption = models.CharField(max_length=20)
    
    def __str__(self):
        return f"{self.caption}"

class LoginModel(models.Model):
    name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=50, blank=True)
    password = models.CharField(max_length=50, blank=True)
    
    def __str__(self):
        return f"{self.name}"
    
class ArticleModel(models.Model):
    name = models.CharField(max_length=50, blank=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to="posts", null=True)
    description = models.CharField(max_length=200, blank=True)
    slug = models.SlugField(unique=True, null=True)
    tag = models.ManyToManyField(TagModel)
    
    def __str__(self):
        return f"{self.name}"
    
class CheckoutModel(models.Model):
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=50, blank=True)
    phone_number = models.IntegerField(blank=True)
    card_number = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(16)], null=True, blank=True)
    mmyy = models.CharField(max_length=5, blank=True)
    cvv = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.first_name}"