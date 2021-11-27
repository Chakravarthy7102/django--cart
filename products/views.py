from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
# index product view


def index(request):
    all_products = Product.objects.all()
    return render(request, 'index.html', {'products': all_products})


# view for new products
def new_products(request):
    string = "new products are here"
    return HttpResponse(string)
