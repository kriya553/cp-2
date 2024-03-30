from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=100)
    category_image = models.ImageField(upload_to="images/",default='')
    # slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.category

class Vendorregistration(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    # username = models.CharField(max_length=100)
    # email = models.CharField(max_length=100)
    # password = models.CharField(max_length=100)
    usertype = models.CharField(max_length=10, default="vendor")

    def __str__(self):
        return str(self.user)
    

class Categorydetails(models.Model):
    categories = (
        ("Photography","Photography"),
        ("Beauty care","Beauty care"),
        ("Occasion","Occasion"),
    )
    vendor = models.ForeignKey(Vendorregistration,on_delete=models.CASCADE)
    category = models.CharField(max_length=100, choices=categories)
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=1000)
    min_price = models.IntegerField()
    max_price = models.IntegerField()
    logo_image = models.ImageField(upload_to="images/",default='')
    # slug = models.SlugField(max_length=100, unique=True)
    services = models.CharField(max_length=1000,blank=True,null=True)
    timing = models.CharField(max_length=1000,blank=True,null=True)
    days = models.CharField(max_length=50,blank=True,null=True)
    location = models.CharField(max_length=1000,blank=True,null=True)
    email = models.CharField(max_length=100,blank=True,null=True)
    image1 = models.ImageField(upload_to = "images/",default='')
    image2= models.ImageField(upload_to = "images/",default='')
    image3 = models.ImageField(upload_to = "images/",default='')
    image4 = models.ImageField(upload_to = "images/",default='')

    def __str__(self):
        return str(self.title) or ''

    # def __str__(self):
    #     return self.title
    
class Booking(models.Model):
    category = models.ForeignKey(Categorydetails,on_delete=models.CASCADE,blank=True,null=True)
    fullname = models.CharField(max_length=100,blank=True,null=True)
    email = models.CharField(max_length=100,blank=True,null=True)
    contactno = models.CharField(max_length=12,blank=True,null=True)
    timing = models.CharField(max_length=1000,blank=True,null=True)
    days = models.CharField(max_length=50,blank=True,null=True)



    
    
    

# class Vendorregistration(models.Model):
#     user = models.OneToOneField(User,on_delete=models.CASCADE)
#     # username = models.CharField(max_length=100)
#     # email = models.CharField(max_length=100)
#     # password = models.CharField(max_length=100)
#     usertype = models.CharField(max_length=10, default="vendor")

#     def __str__(self):
#         return self.user
    
