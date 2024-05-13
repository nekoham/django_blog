from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from rest_framework.views import APIView
from blogs.models import Blog, Comment
from blogs.serializers import TagSerializer, BlogSerializer, CommentSerializer
from django.views.generic import TemplateView


# Create your views here.

class IndexView(TemplateView):
    template_name = 'blogs/index.html'
    
class DetailView(TemplateView):
    template_name = 'blogs/detail.html'

class CreateBlogView(TemplateView):
    template_name = 'blogs/create.html'

class UpdateBlogView(TemplateView):
    template_name = 'blogs/update.html'

class DeleteBlogView(TemplateView):
    template_name = 'blogs/delete.html'

class CreateCommentView(TemplateView):
    template_name = 'comments/create.html'

class UpdateCommentView(TemplateView):
    template_name = 'comments/update.html'

class DeleteCommentView(TemplateView):
    template_name = 'comments/delete.html'
