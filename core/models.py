from django.db import models
from datetime import datetime


class WarehouseProductRel(models.Model):
  warehouse   = models.ForeignKey('core.Warehouse', on_delete=models.CASCADE, verbose_name="المخزن")
  products    = models.ForeignKey('core.Products', on_delete=models.CASCADE, verbose_name="المنتج")
  how_many    = models.IntegerField( verbose_name="الكمية")
  




class ProductTypes(models.base.Model):
  name = models.CharField(max_length=255, verbose_name="اسم")
  desc = models.TextField( blank=True, null=True, verbose_name="الوصف")

  def __str__(self):
    return f"{self.name}"
  
  class Meta:
    
    verbose_name ="نوع المنتج"
    verbose_name_plural ="نوع المنتج"




class saler(models.Model):
  
  name     = models.CharField(max_length=255, verbose_name="اسم البائع")
  phone    = models.CharField(max_length=255, verbose_name="رقم الهاتف",blank=True, null=True)
  addr     = models.TextField(verbose_name="العنوان"                   ,blank=True, null=True)
  isdeb    = models.BooleanField(default=False, verbose_name="دائن؟")
  how_much = models.FloatField(default=0, verbose_name="المقدار")

  
  
  
  def __str__(self):
    return f"{self.name}"
  class Meta:
    
    verbose_name_plural = "البائعون"
    verbose_name = "البائع"
  


class Products(models.Model):
  
  
  p_type     = models.ForeignKey(ProductTypes, on_delete=models.SET_NULL, null=True, verbose_name="نوع المنتج")
  name       = models.CharField(max_length=255, verbose_name="اسم المنتج")
  amount     = models.IntegerField(verbose_name="الكمية")
  salary     = models.FloatField(default=0, verbose_name="سعره للواحد")
  got_it_from= models.ForeignKey(saler, verbose_name='تم شرائه من',  blank=True, null=True, on_delete=models.SET_NULL)
 
  def i_am_in(self):
    rel = WarehouseProductRel.objects.filter(products=self)

    return [x.warehouse for x in rel]

  class Meta:
    
    verbose_name        = "منتجات"
    verbose_name_plural = "منتجات"
  
  def the_rel(self):
    mr = WarehouseProductRel.objects.filter(products=self)
    return mr
  
  @classmethod
  def class_name(cls):
    return "products"

  def __str__(self):
    return f"{self.name}"



class Warehouse(models.Model):
  
  name       = models.CharField(max_length=255, blank=True, default="ware house", null=True, verbose_name="اسم المخزن")
  address    = models.TextField(blank=True, null=True, verbose_name="عنوانه")
  max_amount = models.IntegerField(blank=True, null=True, verbose_name="أقصي كم")
  
  class Meta:
    
    verbose_name_plural = "المخزن"
    verbose_name = "المخزن"
  
  def __str__(self):
    
    return f"{self.name}"
  
  
  def amount_init(self):
    result = 0
    for i in WarehouseProductRel.objects.filter(warehouse=self):
      result += i.how_many
    
    return result
  
  
  def other_obj(self):
    
    pp = Products.objects.all()

    li = []
    for i in pp:
      if len(i.the_rel()) != 0:
        for r in i.the_rel():
            if self == r.warehouse:
              pass
            else:
              li.append(i)
      else:
        try:
          
          m = WarehouseProductRel.objects.get(products=i, warehouse=self)
          v = f'{m.how_many} {m.warehouse.name}'
        except:
          v = "ليس في مخزن"
        li.append([i,v ])

    return li

  def our_obj(self):
    pp = WarehouseProductRel.objects.all()
    li = []
    for i in pp:
      
        if i.warehouse == self:
          
          li.append(i)
        
    return li
  
  @classmethod
  def class_name(cls):
    return "warehouse"

# 



class zabon(models.Model):
  
  name     = models.CharField(max_length=255, verbose_name="اسم الزبون")
  phone    = models.CharField(max_length=255, verbose_name="رقم الهاتف",blank=True, null=True)
  addr     = models.TextField(verbose_name="العنوان"                   ,blank=True, null=True)
  isdeb    = models.BooleanField(default=False, verbose_name="مدين؟")
  how_muchd= models.FloatField(default=0, verbose_name="المقدار")
  

  def __str__(self):
    return f"{self.name}"
  class Meta:
    
    verbose_name_plural = "الزبائن"
    verbose_name = "الزبون"
  
  
  def how_much(self):
    mysales = sales.objects.filter(who_bought=self)
    result = 0
    for i in mysales:
      # try:
        product = Products.objects.filter(name=i.what_got_saled)
        # print(product)
        for s in product:
          # try:
            result += (s.salary * i.how_many)
          # except:
          #   pass
      # except:
      #   pass
    return result

  how_much.short_description = "اجمالي المشتريات"



class sales(models.Model):

  
  what_got_saled = models.ForeignKey(Products, verbose_name='المنتج', null=True, blank=True, on_delete=models.CASCADE)
  how_many       = models.FloatField(default=0, verbose_name='الكمية')
  who_bought     = models.ForeignKey(zabon, verbose_name='الزبون', null=True, blank=True, on_delete=models.CASCADE)
  time_added     = models.DateTimeField(default=datetime.now, editable=False, verbose_name="وقت الاضافة")
  
  


  class Meta:
    
    verbose_name_plural = "المبيعات"
    verbose_name = "بيعة"

  def __str__(self):
    return f"{self.what_got_saled}"







class fwater(models.Model):
  
  
  how_many_fwater   = models.FloatField(verbose_name="مقدار الفاتورة") 
  description_fwater= models.TextField(blank=True,null=True,verbose_name="السبب")
  time_added_fwater = models.DateTimeField(default=datetime.now,verbose_name="وقت اضافة الفاتورة", editable=False)

  
  def __str__(self):
    return f"{self.how_many_fwater}|{self.time_added_fwater}"
  
  class Meta:
    verbose_name= "فاتورة"
    verbose_name_plural = "فواتير"