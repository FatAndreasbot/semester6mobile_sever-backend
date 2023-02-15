from django.shortcuts import render
from rest_framework import generics

from announcement_board.models import Post, Comment
from common.models import Profile

from .serializers import PostSerializer

# Create your views here.


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

