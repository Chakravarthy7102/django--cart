from django.contrib import admin
from .models import Product, Offer


# to manage our products form the admin dashboard..and decide how to display the attributes of a table


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')


admin.site.register(Product, ProductAdmin)
admin.site.register(Offer, OfferAdmin)
