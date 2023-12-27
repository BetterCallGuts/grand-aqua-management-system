from django.contrib import admin
from .models import (Warehouse, 
Products, ProductTypes,
WarehouseProductRel,
sales,
zabon,
saler,
fwater
)
from django.contrib.admin.models import LogEntry

# from django.db.models import Sum, Avg
# Register your models here.


class warehouseProduectRelInine(admin.TabularInline):
  model = WarehouseProductRel
  extra = 0
  verbose_name_plural = "المنتجات داخل المخزن"
  verbose_name        = "منتج"

class ProdTypeRelInline(admin.TabularInline):
  model = Products
  extra = 0
  verbose_name_plural = "المنتجات داخل المخزن"
  verbose_name        = "منتج"


class SalesProduectRelInine(admin.TabularInline):
  model = sales
  extra = 0
  verbose_name_plural = "المبيعات الخاصة بالعنصر"
  verbose_name        = "مبيعات"



class WareHouseProduct(admin.ModelAdmin):
  inlines = (warehouseProduectRelInine,)
  list_display = (
    "name",
    "address",
    "max_amount"
  )
  list_filter = (
    "name", 
    "address",

    
  )
  search_fields =(
    "name",
    "address",
    "max_amount"
  )
  


class ProductAdmin(admin.ModelAdmin):

  list_display = (
    "p_type",
    "name",
    "amount",
    "salary",
    'got_it_from'
  )

  list_filter = (
    "p_type",
    'got_it_from'
  )

  search_fields = (
   
    "name"  ,
    "amount",
    "salary",
    
     
  )


  inlines = (warehouseProduectRelInine,
             SalesProduectRelInine)

class   SalesAdmin(admin.ModelAdmin):
  
  list_display = (
    "what_got_saled",
    "how_many",
    'who_bought',
    "time_added"
  )
  list_filter = (
    "what_got_saled",
   
    "who_bought",
    
  )
  

class zabonAdminStyle(admin.ModelAdmin):
  
  list_display = (
    "name", 
    "phone",
    "how_much",
    "isdeb",
    "how_muchd",
    
  )
  list_filter = (
    "isdeb",
  )
  search_fields  = (
    "name",
    "phone",
    "addr",
    "how_muchd"
  )
  list_tatals = []
  
  inlines = (
    SalesProduectRelInine,
    
    )

class salerAdminStyle(admin.ModelAdmin):
  
  list_display = (
    "name", 
    "phone",
    "isdeb",
    "how_much"
    
  )
  
  search_fields  = (
    "name",
    "phone",
    "addr",
    "how_much"
  )
  list_filter = (
    "isdeb",
    
  )
  
  
class ProductTypeAdmin(admin.ModelAdmin):
  
  inlines = (
    ProdTypeRelInline
    ,)
  
class fwaterAdmin(admin.ModelAdmin):
  
  list_display = (
    "how_many_fwater",
    "time_added_fwater"
  )
  search_fields = (
    "description_fwater",
    "how_many_fwater",
    
  )

admin.site.register(Warehouse   , WareHouseProduct)
admin.site.register(Products    ,ProductAdmin)
admin.site.register(ProductTypes,ProductTypeAdmin)
admin.site.register(zabon       , zabonAdminStyle)
admin.site.register(sales       , SalesAdmin)
admin.site.register(saler       , salerAdminStyle)
admin.site.register(fwater      , fwaterAdmin)
# admin.site.register(LogEntry)
