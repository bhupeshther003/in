from django.contrib import admin
from .models.product import Products
from .models.category import Category
from .models.customer import Customer
from .models.orders import Order
from .models.payment_model import *


class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name']
    
class OrderAdmin(admin.ModelAdmin):
    list_display = ['name']

class Paymentamin(admin.ModelAdmin):
    list_display=['card_number']
    
    
class Paymentmod_upi_Admin(admin.ModelAdmin):
    list_display=['customer']
    
# class Contact_user_Admin(admin.ModelAdmin):
#     list_display=['name']

# Register your models here.
admin.site.register(Products,AdminProduct)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Paymentmod)
admin.site.register(Paymentmod_upi)
# admin.site.register(Contact)



