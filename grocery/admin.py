# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import products,category,orders

# Register your models here.
admin.site.register(products)
admin.site.register(category)
admin.site.register(orders)
