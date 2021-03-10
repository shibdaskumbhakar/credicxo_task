from rest_framework import serializers
from django.contrib.auth.models import User, Group


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('name',)


class UserSerializer(serializers.ModelSerializer):
    # groups = GroupSerializer(many=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'id', 'first_name',
                  'last_name', 'email')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}
