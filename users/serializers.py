from rest_framework import serializers
from .models import User


class UserShortSerializer(serializers.ModelSerializer):
    fullname = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ['fullname', 'email', 'id']

    def get_fullname(self, obj):
        return obj.first_name+' '+obj.last_name


class UserListSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ['email', 'phone', 'name']

    def get_name(self, obj):
        return obj.first_name+' '+obj.last_name