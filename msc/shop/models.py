from django.db import models

class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=100,default='')
    sub_category = models.CharField(max_length=50,default='')
    price = models.FloatField(default='0')
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='shop/images',default='')


    def __str__(self):
        return self.product_name


class Contact(models.Model):
    msg_id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=70,default='')
    phone=models.BigIntegerField()
    desc= models.CharField(max_length=500,default='')

    def __str__(self):
        return self.name

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    item_json = models.CharField(max_length=250)
    amount = models.IntegerField(max_length=100,default=0)
    name = models.CharField(max_length=253)
    email = models.EmailField(max_length=254)
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=521)
    state = models.CharField(max_length=250)
    phone = models.BigIntegerField()
    zip_code = models.IntegerField()

    def __str__(self):
        return self.email

class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default='')
    update_desc = models.CharField(max_length=500)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7]+'...'