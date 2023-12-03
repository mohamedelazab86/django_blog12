# form
from rest_framework import serializers
from .models import Post
from django.contrib.auth.models import User

class Userserializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','email']
        #fields='__all__'


class PostSerializer(serializers.ModelSerializer):
    #author=serializers.StringRelatedField()
    author=Userserializer()
    category=serializers.StringRelatedField()

    class Meta:
        model=Post
        fields='__all__'
