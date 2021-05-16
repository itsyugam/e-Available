# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class products(models.Model):
    cats=(
        ('bodyCare','Body care'),
        ('kitchen','Kitchen ware'),
    )
    store=(
        ('hansuGS','Hansu General Store'),
        ('santuGS','Santu General Store'),
    )
    Id=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=100)
    Brand=models.CharField(max_length=100,default='eGroc')
    Cate=models.CharField(max_length=100,choices=cats)  
    Desc=models.CharField(max_length=500)
    Qty=models.IntegerField(default=99)
    Prize=models.IntegerField() 
    Img=models.ImageField(default='') 
    Store=models.CharField(max_length=100,choices=store,default='')
    
    def __str__(self):
        return self.Name  

class category(models.Model):
    cateName=models.CharField(primary_key=True,max_length=100)
    displayName=models.CharField(max_length=100)
    cateImg=models.ImageField(default='') 
    
    def __str__(self):
        return self.displayName

class store(models.Model):
    storeName=models.CharField(primary_key=True,max_length=100)
    displayStoreName=models.CharField(max_length=100)
    storeImg=models.ImageField(default='') 
    
    def __str__(self):
        return self.displayStoreName 

class orders(models.Model):
    ordId=models.AutoField(primary_key=True)
    ItemDetail=models.CharField(max_length=5000,default="")
    ordName=models.CharField(max_length=100)
    Email=models.CharField(max_length=100)
    Address=models.CharField(max_length=200)  
    City=models.CharField(max_length=100)
    State=models.CharField(max_length=100)
    Pincode=models.CharField(max_length=100)
    Phone=models.CharField(max_length=100)

def __str__(self):
        return self.ordName
