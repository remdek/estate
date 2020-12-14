from rest_framework import serializers
from .models import Location, InputLang

class InputLangSerializer(serializers.ModelSerializer):
    lang = serializers.StringRelatedField()
    class Meta:
        model = InputLang
        fields = ['value', 'lang']


class LocationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['name', 'parent', 'id']