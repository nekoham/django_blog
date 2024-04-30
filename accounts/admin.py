from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import Role, User

from django.contrib import admin

class UserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ["email", "username",]

admin.site.register(User, UserAdmin)
# admin.site.register(Role)

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display=('id', 'name')
    search_fields=('name',)