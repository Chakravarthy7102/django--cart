from django.contrib import admin
from .models import Product

# to manage our products form the admin dashboard..
admin.site.register(Product)
