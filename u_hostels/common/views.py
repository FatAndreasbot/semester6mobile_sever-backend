from django.shortcuts import render
from rest_framework import generics, viewsets

from common.models import Profile, Room, Hostel
from common.serializers import ProfileSerializer, RoomSerializer, HostelSerializer


class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    

class ProfileDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class RoomDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RoomSerializer
    def get_queryset(self):
        profile_id = self.kwargs['pk']
        profileRoomID = Profile.objects.filter(id=profile_id)[0].room.id
        roomQueryset = Room.objects.filter(id = profileRoomID)
        return roomQueryset
    
class HostelList(generics.ListCreateAPIView):
    serializer_class = HostelSerializer
    queryset = Hostel.objects.all()


class HostelRoomList(generics.ListAPIView):
    serializer_class = RoomSerializer
    def get_queryset(self):
        hostelID = self.kwargs['pk']
        queryset = Room.objects.filter(hostel=hostelID)
        return queryset
    
class HostelDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = HostelSerializer
    queryset = Hostel.objects.all()