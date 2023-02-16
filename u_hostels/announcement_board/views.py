from django.shortcuts import render
from rest_framework import generics, viewsets

from announcement_board.models import Post, Comment
from common.models import Profile

from .serializers import PostsSerializer, CommentSerializer

# Create your views here.


class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostsSerializer

class PostDetails(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostsSerializer

class CommentsList(generics.ListAPIView):
    serializer_class = CommentSerializer
    # queryset = Comment.objects.all()
    def get_queryset(self):
        postId = self.kwargs['pk']
        queryset = Comment.objects.filter(post=postId)
        print(postId)
        return queryset