from django.db import models


# Create your models here.
class User(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=20, default='')
    username = models.CharField(max_length=100, default='')
    phone = models.CharField(max_length=15, default='')
    email = models.CharField(max_length=30, default='')
    password = models.CharField(max_length=16, default='')
    role = models.CharField(max_length=10, default='')

class Request_shipping(models.Model):
    id = models.AutoField
    owner_name = models.CharField(max_length=20, default='')
    total_load = models.CharField(max_length=20, default='')
    product = models.CharField(max_length=20, default='')
    origin = models.CharField(max_length=20, default='')
    destination = models.CharField(max_length=20, default='')
    # def __str__(self):
    #     return self.user_name

class Calci(models.Model):
    result = models.IntegerField(default=0)


class Test(models.Model):
    name = models.CharField(max_length=20, default='')
    text = models.CharField(max_length=20, default='')
    username = models.CharField(max_length=100, default='')

    # def __str__(self):
    #     return self.text

    # def get_user_name(self):
    #     return self.user_name
    #
    # def get_user_username(self):
    #     return self.user_username
    #
    # def get_user_phone(self):
    #     return self.user_phone
    #
    # def get_user_email(self):
    #     return self.user_email
    #
    # def get_user_password(self):
    #     return self.user_password
    #
    # def get_user_type(self):
    #     return self.user_type


class Truck(models.Model):
    capacity = models.IntegerField()
    driver_name = models.CharField(max_length=50, default='')
    origin = models.CharField(max_length=50, default='')
    destination = models.CharField(max_length=50, default='')

# class Customer(models.Model):
#     customer_id = models.ForeignKey('login.User', on_delete=models.CASCADE)
#     orders = models.SmallIntegerField(default=0)
#
#
# class Product(models.Model):
#     product_id = models.AutoField
#     product_type = models.CharField(max_length=20)
#     product_name = models.CharField(max_length=50)
#     product_description = models.CharField(max_length=100)
#     product_image = models.ImageField()
#     product_price = models.CharField(max_length=5)
#     product_quantity = models.SmallIntegerField(default=0)
#     product_by = models.ForeignKey('login.User', on_delete=models.CASCADE)
#
#
# class Order(models.Model):
#     order_id = models.AutoField
#     from_customer = models.ForeignKey('login.Customer', on_delete=models.CASCADE)
