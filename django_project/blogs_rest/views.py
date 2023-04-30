from django.shortcuts import get_object_or_404, render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from blog.models import *
from .serializers import PostSerializer


class PostListPagination(PageNumberPagination):
    page_size = 3  # Number of records to display per page

# Create your views for rest api here.
@api_view(['GET'])
def welcome_readers(request):
    welcome_message = {
        'message': 'Welcome readers to my blogs',
        'greeted_by' : 'Badri Paudel'
    }
    return Response(welcome_message)


# Create your models here.
# models for the rest api this time
"""
 Use post class from the another app [blog] here too to render json
"""

# list all the blogs
class PostList(APIView):
    # get as it is going to be a
    def get(self, request):
        post_list = Post.objects.all()
        paginator = PageNumberPagination()
        paginator.page_size = request.GET.get('page_size') # set the number of items per page
        paginator.page = request.GET.get('page')
        paginator.max_page_size = 100
        result_page = paginator.paginate_queryset(post_list, request)
        serializer = PostSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

#  Handle single post [post details]
class PostDetail(APIView):
    # Request type is : GET , so get has been written here.
    def get(self, request, post_id):
        post = get_object_or_404(Post, pk = post_id)
        serializer = PostSerializer(post, many = False)
        return Response(serializer.data)
    
    # Update post title and content with ID {post_id}
    def put(self, request, post_id):
        post = get_object_or_404(Post, pk = post_id)
        updated_title = request.data.get('title')
        updated_content = request.data.get('content')
        if(post):
            post.title = updated_title
            post.content = updated_content
            post.save()
        serializer = PostSerializer(post, many = False)
        return Response(serializer.data)
    
    # delete post with ID {id}
    def delete(self, request, post_id):
        post = get_object_or_404(Post, pk = post_id)
        if(post):
            post.delete()
            deleted_message = {
             "message" : "Post with Id {post_id} deleted successfully".format(post_id = post_id)
            }  
        return Response(deleted_message)