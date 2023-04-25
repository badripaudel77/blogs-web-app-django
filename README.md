
- Install Python
- Create Virtual Environment and activate

  ```
  virtualenv env
  source env/bin/activate
  ```
- Install django

  ```
  pip install django==4.2
  ```
- Create Django Project

  ```
  django-admin startproject django_blog
  ```

  `cd django_blog` where **_manage.py_** is located.
- Migrate [syncs db with models ]

  ```
  python manage.py migrate
  ```
- Run the django Project

  ```
  python manage.py runserver
  ```

  Create the django app [app is complete module]

  `python manage.py startapp blog`
- To Create superuser in python use [for admin access in the url ***/admin***]:

  ```
  python manage.py createsuperuser
  ```

  To render the template, use either render as follows :`returnrender(request, 'blog/index.html', data_dict)`
  where data_dict is key value pair dictionary that we want to pass and access in the template called index.html

  or we can use this as :
- To render the template, use either render as follows :`returnrender(request, 'blog/index.html', data_dict)`
  where data_dict is key value pair dictionary that we want to pass and access in the template called index.html

  ```
  return render(request, 'blog/index.html', data_dict)
  ```

  or use :

  `blog_template = template.loader.get_template('blog/index.html').render(data_dict)`

  `return HttpResponse(blog_template)`
- To include template in another page or location, we can use the following syntax :

  ```
  {% include 'path_to_template_same_as_rendering' %}
  ```

    . Django ORM :

    - To save object to the db,``obj.save()``

    - To delete the object from db,``obj.delete()``

    Django by default adds a manager called`objects` to every model class. The `objects` manager helps us to interact     with the database in complicated ways. The `objects` manager is the most common way Django developers interact with the database. ``ModelClass.objects``

```
Author.objects.all()
```
