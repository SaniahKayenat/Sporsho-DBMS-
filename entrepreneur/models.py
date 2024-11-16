from django.db import models
from django.utils import timezone
# Create your models here.
class Row(models.Model):
    name_of_the_entrepreneur = models.CharField(max_length=30)
    #id = models.IntegerField()
    district = models.CharField(max_length=15)
    upazilla = models.CharField(max_length=15)
    village = models.CharField(max_length=15)
    mobile = models.IntegerField()
    image = models.ImageField( default = 'default.png' , upload_to='entrepreneur/')
    last_updated_date = models.DateTimeField(auto_now= True)
    def __str__(self):
        return f'{self.name_of_the_entrepreneur} : Entrepreneur'
    

class Cow(models.Model):
    name_of_cow = models.CharField(max_length=30,null = True)
    purchase_date = models.DateField()
    breed = models.CharField(max_length=20,null=True)
    color = models.CharField(max_length=15,null=True)
    weight = models.IntegerField(null=True)
    date_of_birth = models.DateField()
    image = models.ImageField(blank=True, upload_to='cow/')
    owner = models.CharField(max_length=30,null=True)

    def __str__(self):
        return f'{self.name_of_cow} : Cow'
    

class Duplicate_cow(models.Model):
    cow_name = models.CharField(max_length=30,blank=True)
    month = models.CharField(max_length=10,default = '',blank = True)
    year = models.CharField(max_length=4,default = '',blank = True)
    dewarming_date = models.DateField()
    torka = models.CharField(max_length=15,blank=True,default='')
    torka_date = models.DateField()
    kurha = models.CharField(max_length=15,blank=True,default='')
    kurha_date = models.DateField(null = True)
    badla = models.CharField(max_length=15,blank=True,default='')
    badla_date = models.DateField()
    name_of_the_disease = models.CharField(max_length=20,blank=True,default='')
    details_on_the_disease = models.CharField(max_length=50,blank=True,default='')
    medications = models.CharField(max_length=30,blank=True,default='')
    monthly_food_expenditure = models.IntegerField(null = True , default=0)
    food_consumed= models.CharField(max_length=150, blank=True)
    percentage_grass=models.IntegerField(default=0,null=True)
    percentage_solid=models.IntegerField(default=0, null=True)
    current_weight = models.IntegerField(default=0,null=True)
    updated_image = models.ImageField(null = True, default='',blank = True, upload_to='cow/')
    def __str__(self):
        return self.month
