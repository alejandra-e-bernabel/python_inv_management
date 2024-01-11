from django.db import models

# Create your models here.

# class Factory(models.Model):
#     name = models.CharField(max_length = 30)

# class Product(models.Model):
#     name = models.CharField(max_length = 10)
#     inventory = models.IntegerField()

class Promotion(models.Model):
    description = models.CharField(max_length = 255)
    discount = models.FloatField()

class Collection(models.Models): 
    title = models.CharField(max_length = 255)
    featured_product = models.ForeignKey('Product', on_delete = models.SET_NULL, null = True, related_name='+')

class Product(models.Model):
    title = models.CharField(max_length = 255)
    description = models.TextField()
    price = models.DecimalField(max_digits = 6, decimal_places = 2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now = True)
    collection = models.ForeignKey(Collection, on_delete = models.PROTECT)
    promotions = models.ManyToManyField(Promotion) #django automatically creates the relationship on the promotion side

    
class Customer(models.Model):
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'
    
    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE, 'Bronze')      #first value is to use in the code, the second value is what the user sees
        (MEMBERSHIP_SILVER, 'Silver')
        (MEMBERSHIP_GOLD, 'Gold')        
    ]
    
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    email = models.EmailField(unique = True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null= True)
    membership = models.CharField(max_length = 1, choices = MEMBERSHIP_CHOICES, default = MEMBERSHIP_BRONZE)
    

class Order(models.Model):
    PAYMENT_PENDING = 'P'
    PAYMENT_COMPLETE = 'C'
    PAYMENT_FAILED = 'F'
    
    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_PENDING, 'Pending')      #first value is to use in the code, the second value is what the user sees
        (PAYMENT_COMPLETE, 'Complete')
        (PAYMENT_FAILED, 'Failed')   
    ]
    
    placed_at = models.DateTimeField(auto_now = True)
    payment_status = models.CharField(max_length = 1, choices = PAYMENT_STATUS_CHOICES, default = PAYMENT_PENDING)
    customer = models.ForeignKey(Customer, on_delete = models.PROTECT)
 
 

class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)
    customer = models.OneToOneField(Customer, on_delete = models.CASCADE)
    

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete = models.CASCADE)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
   

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete = models.SET_NULL)
    product = models.ForeignKey(Product, on_delete = models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits = 6, decimal_max = 2)


class Address(models.Model):
    street = models.CharField(max_length = 255)
    city = models.CharField(max_length = 255)
    customer = models.OneToOneField(Customer, on_delete= models.CASCADE, primary_key = True) #making this key the primary key means that there will only be once adress per customer.

    