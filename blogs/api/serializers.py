from rest_framework import serializers
from blogs.models import Tag, Blog, Comment


class TagSerializer(serializers.ModelSerializer):
    blog_tag = serializers.PrimaryKeyRelatedField(many=True, queryset=Blog.objects.all())

    class Meta:
        model = Tag
        fields = ['blog_tag', 'id', 'name', 'created_on']


class BlogSerializer(serializers.ModelSerializer):
    comment_blog = serializers.PrimaryKeyRelatedField(many=True, queryset=Comment.objects.all())
    user = serializers.ReadOnlyField(source='user.username')
    tag = serializers.ReadOnlyField(source='tag.name')
    
    class Meta:
        model = Blog
        fields = ['comment_blog', 'user', 'tag', 'id', 'name', 'content', 'created_on', 'updated_on']


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    blog = serializers.ReadOnlyField(source='blog.id')

    class Meta:
        model = Comment
        fields = ['user', 'blog', 'id', 'content', 'created_on', 'updated_on']

