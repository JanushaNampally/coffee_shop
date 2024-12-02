from django.contrib import admin # type: ignore
from .models import MenuItem, Customer, Order

admin.site.register(MenuItem)
admin.site.register(Customer)
admin.site.register(Order)
