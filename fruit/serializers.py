from rest_framework import serializers
from .models import Fruit, Supplier


class FruitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fruit
        fields = ['name', 'description', 'price', 'exist', 'supplier']
