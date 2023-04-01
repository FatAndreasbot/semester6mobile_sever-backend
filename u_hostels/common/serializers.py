from rest_framework import serializers
from common.models import Profile, Room, Hostel
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            
            'username',
            'first_name',
            'last_name',
            'last_login',
        )
    
class HostelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hostel
        fields = (
            'id',
            'address',
            'hostelNumber'
        )

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = (
            'hostel',
            'roomNumber'
        )

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            'id',
            'authData',
            'room'
        )