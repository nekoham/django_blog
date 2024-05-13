from rest_framework import generics, status
from blogs.api.serializers import BlogSerializer, CommentSerializer, TagSerializer
from blogs.models import Blog, Comment, Tag
from blogs.permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
import requests
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import (
    MessageEvent,
    TextMessage,
    TextSendMessage,
    StickerMessage,
    StickerSendMessage,
)

# Create your views here.

class IndexData(generics.ListAPIView):
    queryset = Blog.objects.order_by("-created_on")[:10]
    serializer_class = BlogSerializer
    
class DetailData(generics.RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class CreateBlogData(generics.CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        blog_name = self.request.data['name']
        requests.post(url='https://notify-api.line.me/api/notify', data={'message':'A blog named \'{}\' is created.'.format(blog_name)} ,headers={'Authorization': 'Bearer {}'.format('kooGFjl6eNWki8IfGzUYEahCNRl2VKJmDvdc40qBnSd')})
        tagName = self.request.data.get('tag')
        tagObject = Tag.objects.get(name=tagName)
        return serializer.save(user = self.request.user, tag = tagObject)
    
class UpdateBlogData(generics.UpdateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAdminOrReadOnly | IsOwnerOrReadOnly] 

    def perform_update(self, serializer):
        tagName = self.request.data.get('tag')
        tagObject = Tag.objects.get(name=tagName)
        return serializer.save(tag = tagObject)

class DeleteBlogData(generics.DestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAdminOrReadOnly | IsOwnerOrReadOnly] 

class ListCommentData(generics.ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        blog_id = self.kwargs.get('blog_id')
        return Comment.objects.filter(blog=blog_id)

class CreateCommentData(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated] 

    def perform_create(self, serializer):
        return serializer.save(blog_id = self.request.path.split("/")[4], user = self.request.user)

class UpdateCommentData(generics.UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly] 

class DeleteCommentData(generics.DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAdminOrReadOnly | IsOwnerOrReadOnly] 

class DetailCommentData(generics.RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class ListTagData(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

