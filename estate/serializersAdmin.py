from rest_framework import serializers
from .models import Estate, EstateCategory, EstateStatus, EstateProperty, EstatePropertyOption
from users.serializers import UserShortSerializer
from .serializers import EstateCategoryShortSerializer

from locales.mixin.localesMixins import translate_value, translateUpdate


# =========Estate Status=============
class EstateStatusSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    class Meta:
        model = EstateStatus
        fields = ['name', 'id']

    def get_name(self, obj):
        return translate_value(self, obj.name, 'InputLang')


# ===========EstateCategory==============

class EstateCategoryListAdminSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()


    class Meta:
        model = EstateCategory
        fields = ['name', 'title', 'description', 'slug', 'parent', 'id']

    def get_name(self, obj):
        return translate_value(self, obj.name, 'InputLang')


    def get_title(self, obj):
        return translate_value(self, obj.title, 'InputLang')

    def get_description(self, obj):
        return translate_value(self, obj.description, 'TextLang')


class EstateCategoryDetailAdminSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()


    class Meta:
        model = EstateCategory
        fields = '__all__'

    def get_name(self, obj):
        return translateUpdate(self, obj.name, 'InputLang')

    def get_title(self, obj):
        return translateUpdate(self, obj.title, 'InputLang')

    def get_description(self, obj):
        return translateUpdate(self, obj.description, 'TextLang')


# ===============Estate category properties
class EstatePropOptionsListAdminSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = EstatePropertyOption
        fields = '__all__'

    def get_name(self, obj):
        return translate_value(self, obj.name, 'InputLang')


class EstatePropsListAdminSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    options = EstatePropOptionsListAdminSerializer(source='estatePropertyOption_children', many=True)
    class Meta:
        model = EstateProperty
        fields = '__all__'

    def get_name(self, obj):
        return translate_value(self, obj.name, 'InputLang')




class EstatePropsFieldsAdminSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    options = serializers.SerializerMethodField()
    class Meta:
        model = EstateProperty
        fields = '__all__'

    def get_options(self, obj):
        return EstatePropOptionsListAdminSerializer(obj.estatePropertyOption_children, many=True).data

    def get_name(self, obj):
        return translate_value(self, obj.name, 'InputLang')

# ==================Estate Objects==================
class EstateListAdminSerializer(serializers.ModelSerializer):
    country = serializers.StringRelatedField()
    county = serializers.StringRelatedField()
    town = serializers.StringRelatedField()
    district = serializers.StringRelatedField()
    type = EstateCategoryShortSerializer()
    status = EstateStatusSerializer()
    owner = UserShortSerializer()
    broker = UserShortSerializer()

    class Meta:
        model = Estate
        fields = ['address', 'type', 'categories', 'place', 'country',
                  'county', 'town', 'district', 'owner', 'broker', 'status', 'updated', 'id']


class EstateDetailAdminSerializer(serializers.ModelSerializer):
    propsFields = serializers.SerializerMethodField()
    propsValues = serializers.SerializerMethodField()
    class Meta:
        model = Estate
        fields = '__all__'

    def get_propsFields(self, obj):
        data = obj.type.props.values()
        fields = []

        for field in data:
            fields.append(field['id'])
        return fields

    def get_propsValues(self, obj):
        return []




