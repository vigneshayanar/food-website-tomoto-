from django.contrib import admin
from .models import user,menuitem,category,cartitems,cart
# Register your models here.
admin.site.register(user)
admin.site.register(menuitem)
admin.site.register(category)
admin.site.register(cart)
admin.site.register(cartitems)


