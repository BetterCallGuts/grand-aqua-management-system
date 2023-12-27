from django.contrib             import admin
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin  import UserAdmin, GroupAdmin
from .models                    import (
  acc,
  CustomUser,
  CustomGroup,
  
  )


class AccAdminStyle(admin.ModelAdmin):
  
  list_display  = ("name", "salary", "phone_nu", "id_for")

  list_filter   = ("gender", )
  search_fields = ("salary", "name", "phone_nu", "id_for") 
  
  fields        = (
    "pers_pho",
    "photo_for_man",
    "the_acc",
    "name",
    "salary",
    "gender",
    "phone_nu",
    "id_for",
    "date_ofj",
    
  )

  readonly_fields = (
    "photo_for_man",
  )
  

admin.site.unregister(User)
admin.site.unregister(Group)



class CustomUSerAdmin(UserAdmin):pass


admin.site.register(CustomUser, CustomUSerAdmin)
admin.site.register(CustomGroup, GroupAdmin)
admin.site.register(acc , AccAdminStyle)






