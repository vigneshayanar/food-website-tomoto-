from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('sigin/',views.sigin,name='sigin'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('category/',views.Category,name='category'),
    path('menu/<int:pk>',views.menu,name='menu'),
    path('cart/',views.cart_use,name='cart'),
    path('cartpage/',views.cartpage,name='cartpage'),
    path('cartremove/<int:pk>',views.cartremove,name='cartremove'),
    path('paymentsucces/<int:pk>',views.paymentsucces,name='paymentsucces'),




]