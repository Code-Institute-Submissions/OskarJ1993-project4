from django.db import models
from django.contrib.auth.models import User



class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=200)
    slug = models.SlugField(blank=True, null=True)
    image = models.ImageField(upload_to='media')
    category = models.CharField(max_length=100, default="")
    
    def __str__(self):
        return self.title
    
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @classmethod
    def add_to_cart(cls, user, product, quantity):
        cart, created = cls.objects.get_or_create(user=user, product=product)
        if not created:
            cart.quantity += int(quantity)
            cart.save()
        return cart


    