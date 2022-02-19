from django.db import models

# Create your models here.

class Restaurant(models.Model):
    restId = models.AutoField(db_column='restId', primary_key=True)
    restName = models.TextField(db_column='restName')
    phone = models.IntegerField()
    address = models.TextField()
    ratings = models.DecimalField(max_digits=2, decimal_places=1)
    cuisine = models.TextField()
    region = models.TextField()
    last_modify_date = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = "restaurant"

class Employee(models.Model):
    emplid = models.AutoField(db_column='emplid', primary_key=True)
    # restName = models.TextField(db_column='restName')
    name = models.CharField(max_length=50)
   
    city = models.TextField()
    # ratings = models.DecimalField(max_digits=2, decimal_places=1)
    # cuisine = models.TextField()
    # region = models.TextField()
    # last_modify_date = models.DateTimeField(auto_now=True)
    # created = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = "Employee"
