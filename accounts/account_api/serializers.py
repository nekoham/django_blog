from rest_framework import serializers
from accounts.models import Role, User


class RoleSerializer(serializers.ModelSerializer):
    role_user = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all())

    class Meta:
        model = Role
        fields = ['role_user', 'id', 'name']



class UserSerializer(serializers.ModelSerializer):
    role = serializers.ReadOnlyField(source='role.name')

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'date_joined', 'role', 'first_name', 'last_name']
        extra_kwargs = {
            'password': {'write_only': True},  # Exclude password from response
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user
    
    def update(self, instance, validated_data):
        if 'password' in validated_data:
            password = validated_data.pop('password')
            user = super().update(instance, validated_data)
            if password:
                user.set_password(password)
            user.save()
            return user
        return super().update(instance, validated_data)

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=150)