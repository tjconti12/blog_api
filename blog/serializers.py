from .models import Blog
from django.contrib.auth.models import User, Group
from rest_framework import serializers

# Our BlogSerializer
class BlogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'title', 'body']