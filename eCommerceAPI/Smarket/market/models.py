from django.db import models

# Create your models here.

class Order(models.Model):
      order_number=models.CharField(max_length=30)
      order_date = models.DateTimeField(auto_now_add=True)
      username=models.ForeignKey('User',on_delete=models.CASCADE,related_name='user',blank=True)
    #   product=models.ForeignKey('Product',on_delete=models.CASCADE,related_name='product',blank=True)
      status=models.CharField(max_length=30)      
      quantity=models.IntegerField(null=False,default=1)
    #  quantity and price cannot be null or less than 1
      price=models.FloatField(null=False,default=0)
      is_active = models.BooleanField(default=True)
      order_items = models.ManyToManyField('Product',related_name='order_items',blank=True)
      def __str__(self):
         return self.order_date       


class category(models.Model):
    CategoryName = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    def __str__(self):
        return self.name
  
    
class Product(models.Model):
      productName = models.CharField(max_length=30)
      stock = models.CharField(max_length=30)
      price = models.FloatField()
      description = models.CharField(max_length=30)
      image = models.ImageField(upload_to='images/')
      categoryName = models.ForeignKey('category',on_delete=models.CASCADE,related_name='categoryName',blank=True)
      is_active = models.BooleanField(default=True)
      orderNumber=models.ForeignKey('Order',on_delete=models.CASCADE,related_name='product_orders',blank=True)
      #product_orders= models.ManyToManyField('Order',related_name='product_orders',blank=True)
      def __str__(self):
         return self.name
             

class User(models.Model):
    username = models.CharField(max_length=30,null=False,default='username')
    fname = models.CharField(max_length=30,null=True,default='None')
    lname = models.CharField(max_length=30,null=True,default='None')
    age= models.IntegerField(null=True,default='None')
    password = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
   #  user_orders=models.ForeignKey('Order',on_delete=models.CASCADE,related_name='user_orders',blank=True
   #  user_orders= models.ManyToManyField('Order',related_name='user_orders',blank=True)  
    def __str__(self):
        return self.username
         
        return self.name     