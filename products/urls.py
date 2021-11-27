from django.urls import path
from django.urls.resolvers import URLPattern
from . import views


# this is simlar to adding routes in nodejs we are just defining the endpoints setting up the functionality here

urlpatterns = [
    path('', views.index),
    path('new', views.new_products)
]


# all routes and end point that belong to products/ are handled here and
# all this will serve at the djangoApp.urls where they will explicit to the whole application
