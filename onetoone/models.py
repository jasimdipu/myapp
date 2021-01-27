from django.db import models


# Create your models here.

class Place(models.Model):
    place_name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)

    def __str__(self):
        return "place : {}".format(self.place_name)


class Restaurant(models.Model):
    place = models.OneToOneField(Place, on_delete=models.CASCADE, primary_key=True)
    res_name = models.CharField(max_length=50)
    Kacchi = models.BooleanField(default=False)
    Kala_Vuna = models.BooleanField(default=True)
    Beef_Khechuri = models.BooleanField(default=True)

    def __str__(self):
        return "Restaurant : {}, place : {}".format(self.res_name, self.place.place_name)
