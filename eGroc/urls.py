"""eGroc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
#from django.conf.urls import url,include
from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from grocery import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('productByCat/<str:Categ>' , views.productsByCat, name='productByCat'),
    path('productByStore/<str:StoreName>' , views.productsByStore, name='productByStore'),
    path('productView/<int:id>' , views.prodView, name='productView'),
    path('cart/', views.cart, name='myCart'),
    path('checkout/' , views.checkout, name='checkout'),
    path('about/' , views.about, name='about'),
    path('contact/' , views.contact, name='contact'),
    
 ]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
