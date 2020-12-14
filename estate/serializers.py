from rest_framework import serializers
from .models import Estate, EstateCategory
from locales.mixin.localesMixins import translate_value




#================= Category Estate
class EstateCategoryShortSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = EstateCategory
        fields = ['name', 'id']

    def get_name(self, obj):
        return translate_value(self, obj.name, 'InputLang')


class RecursiveSerializer(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class EstateCategoryTreeSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    children = RecursiveSerializer(many=True, read_only=True, source='estateCategory_children_new')

    class Meta:
        model = EstateCategory
        fields = ['name', 'children', 'parent', 'id']

    def to_representation(self, data):
        data.estateCategory_children_new = data.estateCategory_children
        return super(EstateCategoryTreeSerializer, self).to_representation(data)

    def get_name(self, obj):
        return translate_value(self, obj.name, 'InputLang')

