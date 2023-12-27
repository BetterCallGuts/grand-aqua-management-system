# from django.shortcuts import render, redirect
# from django.http      import HttpRequest
# from .models          import Warehouse, Products, ProductTypes, WarehouseProductRel
# from django.contrib   import messages
# from django.urls      import reverse
# from django.contrib.auth.decorators import login_required


# modules_avalable  = [
#       # 'sales',
#       # 'hr',
#       # 'calculation',
#       Warehouse,
#       Products
#       ]

# @login_required(login_url="")
# def index(req:HttpRequest):
  

    
#   return render(req, "main/pages/landing_page.html")
  



# @login_required(login_url="")
# def overview_page(req, module):
  
  
#   data = {
#     'chosen' : module,
#   }
  
#   return render(req, "main/pages/modules_pages/overview.html", data)


# @login_required(login_url="")
# def detail_page(req,   module, pk):
  
  
#     data = {
#       'chosen' : module,
#     }
    
    
  
  
    
    
#     in_ = True
#     for s in modules_avalable:

#       if module == s.class_name():
#         if req.method == "POST":
#           if req.POST['type'] == "edit":
#             u = {}
#             for i in req.POST:
#               if in_:
                
#                 in_ = False
#                 continue
#               u[f"{i}"] = req.POST[f"{i}"]
#             if module == "products":
#               print(u)
#               pk_from_form = u['p_type']
#               u['p_type'] = ProductTypes.objects.get(pk=int(pk_from_form))

#             for k in u:
#               print(type(u[k]))
#               if u[f"{k}"] == "":
#                 u[f"{k}"] = None
#             ob = s.objects.get(pk=pk)
#             l = {}
#             u.pop('type')
#             for k in u:
#               if u[k] is not None:
#                 exec(f"l['{k}'] = ob.{k}  ")
            
#             s.objects.update_or_create(**l,defaults=u)
            


#             data['data'] = s.objects.get(pk=pk)
#             messages.success(req, "تم التعديل بنجاح")
#           elif req.POST['type'] == "outside":

#             ware         = s.objects.get(pk=pk)
#             data['data'] = ware
#             in_ = True
#             made = True
#             a   = 0
#             for i in req.POST:
#               if in_:
#                 a +=1
#                 if a ==2 :
#                   in_ = not in_
#               else:
#                 made = False
#                 pro = Products.objects.get(pk=int(i))          
#                 rel = WarehouseProductRel.objects.create(warehouse=ware, products=pro,how_many=pro.amount )
#                 rel.save()
#             if not made:
#               messages.success(req, "لقد أدخلت العناصر بنجاح")
#               # 
#           elif req.POST['type'] == "inside":
#             ware         = s.objects.get(pk=pk)
#             data['data'] = ware
#             in_ = True
#             made= True
#             a   = 0
#             for i in req.POST:
#               if in_:
#                 a +=1
#                 if a ==2 :
#                   in_ = not in_
#               else:
#                 made = False
#                 pro = Products.objects.get(pk=int(i))          
#                 rel = WarehouseProductRel.objects.get(warehouse=ware, products=pro,how_many=pro.amount )
#                 rel.delete()
#             if not made:
#               messages.success(req, "لقد أخرجت العناصر بنجاح")
#         else:
#           data['data'] = s.objects.get(pk=pk)
#     if s.class_name() == "products":
#       data['more'] = ProductTypes.objects.all()
#       the_p        = data['data']
#       try:
        
#         the_rel      = WarehouseProductRel.objects.get(products=the_p)
#         the_war      = the_rel.warehouse
#         x            = True
#       except:
#         x            = False
#         the_war      = "المنتج ليس في مخزن"
#       data['ware'] = the_war
#       data['x']    = x
    

#     return render(
#       req,
#       "main/pages/modules_pages/detailview.html",
#       data
#       )


# # 
# @login_required(login_url="")
# def list_page(req:HttpRequest,     module:str):

#   data = {
#     'chosen' : module,
#   }
  
#   for i in modules_avalable:
    
    
#     if i.class_name() == module:

      
      
#         data["data"] = i.objects.all()
      
  
  
  
#   return render(req, "main/pages/modules_pages/listview.html", data)
# @login_required(login_url="")
# def add_page(req,      module):
#   data = {
#     'chosen' : module,
#   }
#   if req.method == "POST":
    
    
#     in_ = True
#     for s in modules_avalable:

#       if module == s.class_name():
#         u = {}
#         for i in req.POST:
#           if in_:
            
#             in_ = False
#             continue
#           u[f"{i}"] = req.POST[f"{i}"]
#         if module == "products":
#           pk_from_form = u['p_type']
#           u['p_type'] = ProductTypes.objects.get(pk=int(pk_from_form))
          
#         for k in u:
#           if u[f"{k}"] == "":
#             u[f"{k}"] = None
#         ob = s.objects.create(**u)

#         ob.save()
#         messages.success(req, "تم اضافة العنصر بنجاح")
#         return redirect(reverse("core:list-view", args=[s.class_name()]))

#   if module == "products":
#         data['more'] = ProductTypes.objects.all()
#   return render(req, "main/pages/modules_pages/addview.html", data)





# @login_required(login_url="")
# def delete_view(req, module):
  
#   in_ = True
#   done= False
#   for s in modules_avalable:
#     print(module, s)
#     if module == s.class_name():
#       print("The module is correctin")
#       for i in req.POST:
#         if in_:
          
#           in_ = False
#           continue
#         print(i)
#         s.objects.get(pk=int(i)).delete()
#         done = True

#     if done:
#       messages.success(req, "لقد مسحت العناصر المحددة بنجاح")
#       break
#   return redirect(f"core:list-view", module)
  



# # Hp smart tank 515