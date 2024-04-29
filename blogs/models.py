from django.db import models
from accounts.models import Users
# Create your models here.
    
class Tags(models.Model):
    tag = models.CharField(max_length=20, help_text="Tag's name")
    created_on = models.DateTimeField(auto_now_add=True, help_text="Date of creation")

    def __str__(self):
        return self.tag
    
class Blogs(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tags, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=30, help_text="Blog's name")
    content = models.TextField(help_text="Blog's content")
    created_on = models.DateTimeField(auto_now_add=True, help_text="Date of creation")
    updated_on = models.DateTimeField(auto_now=True, help_text="Date of update")


    def __str__(self):
        return self.name
    
class Comments(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blogs, on_delete=models.CASCADE)
    content = models.TextField(help_text="Comment's content")
    created_on = models.DateTimeField(auto_now_add=True, help_text="Date of creation")
    updated_on = models.DateTimeField(auto_now=True, help_text="Date of update")



