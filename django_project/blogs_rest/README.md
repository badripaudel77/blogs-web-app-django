This is for developing REST API using django

---

- Create a brand new django project if you have not already using the command called : ``django-admin startproject projectname``
- Now, create a new app called **blogs_rest** using command called ``python manage.py startapp blogs_rest``
- Now install django rest framework as : ``pip install djangorestframework``
- Add **blogs_rest** to the list of INSTALLED_APPS in ``settings.py``
- Include ``blogs_rest`` , ``rest_framework`` in settings.py under INSTALLED_APPS.
- Define url as ``path('api/v1/blogs/welcome/', blogs_rest.welcome_readers, name = 'blogs_rest_welcome'),`` for function based and  ``path('api/v1/blogs/list/', blogs_rest.PostList.as_view(), name = 'blogs_list')`` for class based

  Need to define serializer as [ an example ]:

  ```

  class PostSerializer(serializers.ModelSerializer):
       class Meta:
          model = Post # from the model class Post
          # fields = '__all__' # include all the fields in json response
          fields = ['title', 'slug', 'content', 'img_url', 'pub_date', 'author', 'category', 'tags', 'views_count', 'likes_count']

  ```
- And actual request as :

  ```
     # Request type is : GET , so get has been written here.
      def get(self, request, post_id):
          print('----- details ------ ', post_id)
          post = get_object_or_404(Post, pk = post_id)
          serializer = PostSerializer(post, many = False)
          return Response(serializer.data)
  ```
- for get request, it's get, for put it's put and for delete it's delete.
- Now rest is very similar such as views.py, models , urls.py etc.
