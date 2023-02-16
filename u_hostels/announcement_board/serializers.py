from rest_framework import serializers
from announcement_board.models import Post, Comment, Tags
from common.models import Profile
from common.serializers import ProfileSerializer


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = [
            'name'
        ]


class PostsSerializer(serializers.ModelSerializer):
    author = ProfileSerializer(many=False, read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'author',
            'created',
            'img',
            'tags'
        ]
    

class CommentSerializer(serializers.ModelSerializer):
    author = ProfileSerializer(many=False, read_only=True)
    class Meta:
        model = Comment
        fields = [
            'author',
            'text',
            #'post'
        ]

