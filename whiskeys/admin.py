from django.contrib import admin
from .models import Whiskey, Flavor, Drink

# Register your models here.
admin.site.register(Whiskey)
admin.site.register(Flavor)
admin.site.register(Drink)