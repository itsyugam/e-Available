# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import products,category,orders,store
import pandas
import json

# Create your views here.
def index(requests):
   s=store.objects.all()
   c=category.objects.all()
   params={'category':c,'store':s}
   return render(requests,'index.html',params)

def productsByStore(requests,StoreName):
   prod_list=products.objects.filter(Store=StoreName)
   params={'product':prod_list}
   return render(requests,'allproducts.html',params)

def productsByCat(requests,Categ):
   prod_list=products.objects.filter(Cate=Categ)
   params={'product':prod_list}
   return render(requests,'allproducts.html',params)

def prodView(requests,id):
   prodDetail=products.objects.filter(Id=id)
   params={'pd':prodDetail}
   return render(requests,'prodView.html',params)

def cart(requests):
   return render(requests, 'myCart.html')

def checkout(requests):
   placed=0
   if requests.method=="POST":
      cart=requests.POST.get("cart")
      name=requests.POST.get("name")
      email=requests.POST.get("email")
      address=requests.POST.get("add1")+requests.POST.get("add2")
      state=requests.POST.get("state")
      city=requests.POST.get("city")
      pincode=requests.POST.get("pincode")
      phone=requests.POST.get("phone")
      print(cart,name,email,address,state,city,pincode,phone)
      obj=orders(ordName=name,ItemDetail=cart,Email=email,Address=address,City=city,State=state,Pincode=pincode,Phone=phone)
      obj.save()
      placed=1
      return render(requests, 'checkout.html',{"placed":placed})
   return render(requests, 'checkout.html',{"placed":placed})

def about(requests): 
   return render(requests,'about.html')

def contact(requests):
   return render(requests,'contact.html')
