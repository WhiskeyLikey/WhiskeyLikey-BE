from django.db import models

def whiskey_upload_path(instance, filename):
    return f'whiskey/{instance.pk}/{filename}'

def flavor_upload_path(instance, filename):
    return f'flavor/{instance.pk}/{filename}'

def drink_upload_path(instance, filename):
    return f'drink/{instance.pk}/{filename}'

    
class Flavor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to=flavor_upload_path, blank=True, null=True)

    def __str__(self):
        return self.name
    
class Drink(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to=drink_upload_path, blank=True, null=True)

    def __str__(self):
        return self.name

class Whiskey(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField()
    whiskey_image = models.ImageField(upload_to=whiskey_upload_path, blank=True, null=True)
    flavor = models.ManyToManyField(Flavor, blank=True)
    drink = models.ManyToManyField(Drink, blank=True)

    def __str__(self):
        return self.name

