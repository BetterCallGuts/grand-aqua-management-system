from django.shortcuts          import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.http               import HttpRequest
from django.contrib.auth       import logout, login
# from django.urls               import reverse


def login_page(req:HttpRequest):
  
  if req.user.is_authenticated:
    return redirect('core:landing')

  
  if req.method == "POST":
    form = AuthenticationForm(req, data=req.POST)
    
    if form.is_valid():
      
      login(req, form.get_user())

      return redirect('core:landing')
    else:
      
      form  = AuthenticationForm()
      error = "تأكد من اسمك و كلمة المرور"
      
      data = {
        'form' : form,
        "error" : error
      }
      return render(req, "main/auth_pages/login.html", data)

    
  form  = AuthenticationForm()
  
  
  data = {
    'form' : form
  }
  return render(req, "main/auth_pages/login.html", data)




def logout_page(req:HttpRequest):
  
  logout(req)
  
  return render(req, "main/auth_pages/logout.html")
