from rest_framework import serializers
from .models import User, Group, UserContacts

class UserContactsAdminSerializer(serializers.SerializerMethodField):
    class Meta:
        model = UserContacts
        fields = '__all__'

class UserGroupListAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

class UserDetailAdminSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ['password']




class UserListAdminSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    group = UserGroupListAdminSerializer(many=True)
    class Meta:
        model = User
        fields = ['email', 'phone', 'name', 'group', 'block', 'created', 'id']

    def get_name(self, obj):
        return obj.first_name+' '+obj.last_name

