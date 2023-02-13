from rest_framework import serializers
from announcement_board.models import Post, Comment
from common.models import Profile
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'last_login',
        )

class ProfileSerializer(serializers.ModelSerializer):
    authData = UserSerializer(many=False, read_only=True)
    class Meta:
        model = Profile
        fields = (
            'authData',
        )

class PostSerializer(serializers.ModelSerializer):
    author = ProfileSerializer(many=False, read_only=True)
    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'author',
            'created',
            'img',
        )