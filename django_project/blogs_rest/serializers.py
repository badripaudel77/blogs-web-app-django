"""
This class is responsible for converting complex data types such as Django models
or querysets into JSON, XML, or other content types that can be easily consumed 
by web clients.
"""

from blog.models import *

from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
     class Meta:
        model = Post # from the model class Post
        # fields = '__all__' # include all the fields in json response
        fields = ['title', 'slug', 'content', 'img_url', 'pub_date', 'author', 'category', 'tags', 'views_count', 'likes_count']
