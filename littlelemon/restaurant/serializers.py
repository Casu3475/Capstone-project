from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Menu, Booking


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'title', 'price', 'inventory']


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'


class GroupNameField(serializers.StringRelatedField):
    def to_representation(self, value):
        # Return the group name
        return value.name


class UserSerializer(serializers.ModelSerializer):
    groups = GroupNameField(many=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['groups'].queryset = self.instance.groups.all()
