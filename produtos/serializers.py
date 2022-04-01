from rest_framework import serializers

from .models import Region, Fruit


class RegionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Region
        fields = (
            'id',
            'name'
        )


class FruitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Fruit
        fields = (
            'id',
            'region',
            'nameFruit'
        )