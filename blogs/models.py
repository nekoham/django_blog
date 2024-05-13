from django.db import models
from accounts.models import User
# Create your models here.
    
class Tag(models.Model):
    name = models.CharField(max_length=20, help_text="Tag's name")
    created_on = models.DateTimeField(auto_now_add=True, help_text="Date of creation")

    def __str__(self):
        return self.name
    
class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_user")
    tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True, related_name="blog_tag")
    name = models.CharField(max_length=30, help_text="Blog's name")
    content = models.TextField(help_text="Blog's content")
    created_on = models.DateTimeField(auto_now_add=True, help_text="Date of creation")
    updated_on = models.DateTimeField(auto_now=True, help_text="Date of update", null=True)

    def __str__(self):
        return self.name
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment_user")
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="comment_blog")
    content = models.TextField(help_text="Comment's content")
    created_on = models.DateTimeField(auto_now_add=True, help_text="Date of creation")
    updated_on = models.DateTimeField(auto_now=True, help_text="Date of update")

    def __str__(self):
        return self.content


