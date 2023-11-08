from django.contrib import admin
from .models import Whiskey, Flavor, Drink, UserNumbers

# Register your models here.
admin.site.register(Whiskey)
admin.site.register(Flavor)
admin.site.register(Drink)
admin.site.register(UserNumbers)