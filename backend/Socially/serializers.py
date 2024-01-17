from .models import Post, Blog, LoginUser, RegisterUser
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields="__all__"

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model=Blog
        fields="__all__"

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoginUser
        fields="__all__"

class RegisterSerializer(APIView):
    class Meta:
        model = RegisterUser
        fields = "__all__"

