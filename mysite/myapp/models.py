from django.db import models

# Create your models here.

class menue(models.Model):
    foodtime=models.CharField( max_length=100,choices=(('B','Breakfast'),('L','Launch'),('D','Dinner')))
    foodname = models.CharField(max_length=100)
    foodprice = models.CharField(max_length=100)
    image = models.ImageField(upload_to='uploads', verbose_name='image')


