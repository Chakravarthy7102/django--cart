from django.http import HttpResponse
from django.shortcuts import render

# index product view


def index(request):
    string = 'hello world ,this is my first django application'
    return HttpResponse(string)


# view for new products
def new_products(request):
    string = "new products are here"
    return HttpResponse(string)
