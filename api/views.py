from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import UserProfile, Post, Comment
from .serializers import UserProfileSerializer, PostSerializer, CommentSerializer
from django.contrib.auth.models import User

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_profile(request, user_id):
    user_profile = get_object_or_404(UserProfile, user_id=user_id)
    serializer = UserProfileSerializer(user_profile)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow_user(request, user_id):
    user_profile = get_object_or_404(UserProfile, user_id=request.user.id)
    follow_u=get_object_or_404(User,id=user_id)
    user_profile.followers.add(follow_u)
    return Response({'message': 'You are now following this user.'})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unfollow_user(request, user_id):
    user_profile = get_object_or_404(UserProfile, user_id=request.user.id)
    unfollow_u=get_object_or_404(User,id=user_id)
    user_profile.followers.remove(unfollow_u)
    return Response({'message': 'You are not following this user.'})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_detail(request):
    user = request.user
    return Response({
        'username': user.username,
        'follower_count': UserProfile.objects.filter(followers__id=user.id).count(),
        'following': user.userprofile.followers.all()
    })

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def upload_post(request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(created_by=request.user)
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def all_posts(request):
    posts = Post.objects.filter(created_by=request.user)
    serializer = PostSerializer(instance=posts, many=True)
    return Response(serializer.data)

@api_view(['GET', 'DELETE'])
@permission_classes([IsAuthenticated])
def get_or_delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'GET':
        return Response(data=PostSerializer(instance=post).data)
    if post.user == request.user:
        post.delete()
        return Response({'message': 'Post deleted.'})
    return Response({'error': 'You are not authorized to delete this post.'}, status=401)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.liked_by.add(request.user)
    return Response({'message': 'Post liked.'})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unlike_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.liked_by.remove(request.user)
    return Response({'message': 'Post unliked.'})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comment_on_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user, post=post)
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
