from rest_framework import serializers
from .models import UserProfile, Post, Comment

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['user', 'bio', 'profile_picture','followers']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, required=False)
    likes = serializers.IntegerField( required=False)
    class Meta:
        model = Post
        fields = ['id', 'title', 'description', 'created_at', 'comments', 'likes']
        read_only_fields = ['id', 'created_by', 'created_at','comments','likes']

