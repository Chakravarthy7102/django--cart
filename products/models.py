from django.db import models

# creating a model means to create the object representaton of the models we are gonna use inside our application
# always use max_length field for the security purposes
# preventing from entering that is too large to handle


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    stock = models.IntegerField()
    # 2083 is the stardard max length for a url that means a urls in worst case wont be exceeding that limit
    image_url = models.CharField(max_length=2083)


class Offer(models.Model):
    code = models.CharField(max_length=12)
    description = models.CharField(max_length=200)
    discount = models.FloatField()


# points to be notted for making the migration changes
# and creating the tables dynamically inside the database
# after creating  the models to create a databse table dynamicalyy use
# win: python manage.py makemigrations
# mac: python3 manage.py makemigrations
# to create a data table inside the database run command
# win: python manage.py migrate
# mac :python3 manage.py migrate
