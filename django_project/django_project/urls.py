"""
URL configuration for django_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog import views as blog_views
from blogs_rest import views as blogs_rest

from rest_framework import routers
from rest_framework.authtoken import views
from django.urls import include, path

from blogs_rest import views as blogs_rest

router = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),

    # need to add url pattern here with the method from the view of the respected app
    path('', blog_views.index, name = 'blog_index_page'), 
    path('blogs/details/<int:post_id>', blog_views.get_post_details, name = 'blog_details'),
    path('blogs/details/<int:post_id>/comment', blog_views.post_comment, name = 'blog_details'),
    path('blogs', blog_views.get_blogs),
    path('author/<int:author_id>/blogs', blog_views.all_posts_of_author, name = "author_blogs" ),
    path('today', blog_views.date_today, name = 'blog_time_today'), 

    # urls for rest API
    # optional but useful 
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', views.obtain_auth_token),
    path('', include(router.urls)),
    path('api/v1/blogs/welcome/', blogs_rest.welcome_readers, name = 'blogs_rest_welcome'),
    path('api/v1/blogs/list/', blogs_rest.PostList.as_view(), name = 'blogs_list'),
    path('api/v1/blogs/<int:post_id>/details', blogs_rest.PostDetail.as_view(), name = 'blog_details'),
]
