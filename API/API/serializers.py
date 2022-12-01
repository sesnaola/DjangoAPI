from rest_framework import serializers
from .models import Drink
# Transform the data into JSON format


class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = ('id', 'name', 'description')
