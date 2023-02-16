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
            'address',
            'hostelNumber'
        )

class RoomSerializer(serializers.ModelSerializer):
    hostel = HostelSerializer(many=False)
    class Meta:
        model = Room
        fields = (
            'hostel',
            'roomNumber'
        )

class ProfileSerializer(serializers.ModelSerializer):
    authData = UserSerializer(many=False, read_only=True)
    room = RoomSerializer(many=False)
    class Meta:
        model = Profile
        fields = (
            'id',
            'authData',
            'room'
        )