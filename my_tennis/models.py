from django.db import models

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
class Student(models.Model):
  name = models.CharField(max_length=255)
  roll = models.CharField(max_length=255)
  stu_id = models.CharField(max_length=255)
class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    category= models.CharField(max_length=50, default="")
    sub_category= models.CharField(max_length=50, default="")
    price=models.IntegerField(default=0)
    desc=models.CharField(max_length=300)
    pub_date=models.DateField()
    image= models.ImageField(upload_to="my_tennis/images",default="")
    def __str__(self):
        return self.product_name
    