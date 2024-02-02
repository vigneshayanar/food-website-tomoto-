from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.
class user(models.Model):
    name=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    email=models.EmailField(max_length=20)

class category(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='images/',default=True)

    def __str__(self):
        return self.name

class menuitem(models.Model):
    name=models.CharField(max_length=200)
    description=models.CharField(max_length=200)
    image=models.ImageField(upload_to='images/')
    price=models.DecimalField(max_digits=5,decimal_places=2)
    category=models.ForeignKey(category,on_delete=models.CASCADE,default=1)
     
    def __str__(self):
        return self.name
    
    
class cart(models.Model):
    id=models.UUIDField(default=uuid.uuid4,primary_key=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    completed=models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)


    
class cartitems(models.Model):
    menu=models.ForeignKey(menuitem,on_delete=models.CASCADE)
    cartitems=models.ForeignKey(cart,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=0)

    
    def __str__(self):
            return f"{self.menu.name} - {self.quantity}"
    

    @property
    def prize(self):
        new_prize=self.menu.price * self.quantity
        return new_prize
    
    @property
    def total_prize(self):
        cartitems=self.cartitems.all()
        total=sum([item.price for item in cartitems])
        return total
    

