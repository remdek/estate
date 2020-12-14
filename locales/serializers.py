from rest_framework import serializers
from .models import Location, InputLang, TextLang

class InputLangSerializer(serializers.ModelSerializer):
    lang = serializers.StringRelatedField()
    class Meta:
        model = InputLang
        fields = ['value', 'lang', 'id']

class TextLangSerializer(serializers.ModelSerializer):
    lang = serializers.StringRelatedField()
    class Meta:
        model = TextLang
        fields = ['value', 'lang', 'id']


class LocationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['name', 'parent', 'type', 'id']