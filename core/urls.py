from django.urls import path
from .           import views
from .auth_handler.views import login_page, logout_page


app_name = "core"

urlpatterns = [
path('', login_page, name='login'),
path('logout/', logout_page, name='logout'),






path("POS/", views.pos, name="pos"),
path("add_pos_cart/", views.add_pos_cart, name="add_pos_cart")

]
