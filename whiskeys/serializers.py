from rest_framework import serializers
from .models import Whiskey, UserNumbers

class UserNumbersSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserNumbers
        fields = ['number']

class WhiskeySerializer(serializers.ModelSerializer):

    flavor = serializers.SerializerMethodField()
    def get_flavor(self, instance):
        flavors = instance.flavor.all()
        flavors_names = [f.name for f in flavors]
        return flavors_names
    
    flavor_images = serializers.SerializerMethodField()
    def get_flavor_images(self, instance):
        request = self.context.get('request')
        flavors = instance.flavor.all()
        flavors_images = []

        for f in flavors:
            image_url = request.build_absolute_uri(f.image.url)
            flavors_images.append(image_url)

        return flavors_images
    
    drink = serializers.SerializerMethodField()
    def get_drink(self, instance):
        drinks = instance.drink.all()
        drinks_names = [d.name for d in drinks]
        return drinks_names
    
    drink_images = serializers.SerializerMethodField()
    def get_drink_images(self, instance):
        request = self.context.get('request')
        drinks = instance.drink.all()
        drinks_images = []

        for d in drinks:
            image_url = request.build_absolute_uri(d.image.url)
            drinks_images.append(image_url)

        return drinks_images

    class Meta:
        model = Whiskey
        fields = [
            'name',
            'description',
            'whiskey_image',
            'flavor',
            'flavor_images',
            'drink',
            'drink_images',
        ]