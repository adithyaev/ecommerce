from django.db import models

# Create your models here.
class Seller(models.Model):
    first_name = models.CharField(max_length=25)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    company_name = models.CharField(max_length=25)
    email = models.CharField(max_length=25)
    gender = models.CharField(max_length=25)
    city = models.CharField(max_length=25)
    country = models.CharField(max_length=25)
    password = models.CharField(max_length=25)
    profile_image = models.ImageField(upload_to="seller/")
    login_id = models.IntegerField(null=True)
    account_name = models.BigIntegerField()
    bank_name = models.CharField(max_length=20)
    ifsc_code = models.CharField(max_length=20)
    status = models.CharField(max_length=50,default='pending')
    
    class Meta:
        db_table = 'seller_tb'
    
    
