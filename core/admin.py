from typing import Any
from django.contrib import admin
from .models import (Warehouse, 
Products, ProductTypes,
WarehouseProductRel,
sales,
zabon,
saler,
fwater,
Shop,
Factory

)
from rangefilter.filters import DateRangeFilterBuilder

from django.contrib.admin.models import LogEntry

# from django.db.models import Sum, Avg
# Register your models here.

# inlines
# -----------------------------------------
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

# simplelistfilter
# ------------------------

class ProductsFilter(admin.SimpleListFilter):
  
  title = "المنتج"
  parameter_name = "product"
  
  def lookups(self, req, modeladmin) -> list[tuple[Any, str]]:
    
    products_objects = Products.objects.all()
    
    returned_list = [
      (f"{i.pk}", f"{i}") for i in products_objects
    ]

    return returned_list
  
  def queryset(self, request, queryset):
   
    if self.value():
      
      returned_list = []
      item = Products.objects.get(pk=int(self.value()))
      

      for shop in queryset:
          
          if item.shop_in == shop:
            print("if happened")
            returned_list.append(shop.id)
            
      

      return queryset.filter(id__in=returned_list)
    else: 
      return queryset


# modeladmin
# --------------------------------------
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
    'got_it_from',
    "shop_in",
  )

  list_filter = (
    "p_type",
    'got_it_from',
    "shop_in",
  )

  search_fields = (
   
    "name"  ,
    "amount",
    "salary",
    
     
  )


  inlines = (warehouseProduectRelInine,
             SalesProduectRelInine)
# POS
# --------------
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
    ("time_added",DateRangeFilterBuilder()),
    
    
  )
  
  change_list_template = "mine/sales__mine.html"
  change_form_template = "mine/sales__formmine.html"
# End POS
# -------------------
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
  list_filter = (
    ("time_added_fwater", DateRangeFilterBuilder()),
  )


class ShopAdminStyle(admin.ModelAdmin):
  
  list_display = (
    "name",
    "how_many_in_me",
  )
  inlines      = ( ProdTypeRelInline,)
  list_filter  = (ProductsFilter,)



class FactoryAdminStyle(admin.ModelAdmin):
  list_display = (
    "name", 
    "spic",
  )
  
  list_filter = (
    "spic",
    
  )

  search_fields = (
    "name",
    "addr",
    
  )


admin.site.register(Warehouse   , WareHouseProduct)
admin.site.register(Products    , ProductAdmin)
admin.site.register(ProductTypes, ProductTypeAdmin)
admin.site.register(zabon       , zabonAdminStyle)
admin.site.register(sales       , SalesAdmin)
admin.site.register(saler       , salerAdminStyle)
admin.site.register(fwater      , fwaterAdmin)
admin.site.register(Shop        , ShopAdminStyle)
admin.site.register(Factory     , FactoryAdminStyle)

# admin.site.register(LogEntry)``

