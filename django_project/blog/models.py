from django.db import models

# Create your models here.
# models related to blog post

# Representing the Author of the post
class Author(models.Model):
    # verbose_name="Author Name" changes label or overrides default django label.
    name = models.CharField(max_length = 100, unique = False, verbose_name="Author Name", help_text = "Enter the name of the author")
    email = models.EmailField(max_length = 200, unique = True, help_text = "Enter valid email")
    active = models.BooleanField(default = False, help_text = "If you set False, account will be deactivated.")
    created_on = models.DateTimeField(auto_now_add = True)
    last_logged_in = models.DateTimeField(default = None)

    
# Indicating Category of the post
class Category(models.Model):
     name = models.CharField(max_length=100, unique=True, help_text = "Enter one word category or name seperated by - or _")
     # blank=True, makes field optional
     slug = models.SlugField(max_length=100, unique=True, blank=True)
     """
       If Author is deleted, cateogry of that particular author is also deleted. 
     """
    #  author = models.ForeignKey(Author, on_delete = models.CASCADE)

    #If author is deleted, category will not be deleted, instead author field of that category will be set null
     author = models.ForeignKey(Author, null=True, on_delete = models.SET_NULL)
     created_on = models.DateTimeField(auto_now_add = True)

     """By default python Makes plural as Categorys, to change it to something meaningful, we need to do this"""
     class Meta:
         verbose_name_plural = "Categories"


# Representing tag of the particular post
class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, blank=True, unique=True, help_text = "slug will be generated automatically from the title of the post")
    author = models.ForeignKey(Author, on_delete = models.CASCADE)
    created_on = models.DateTimeField(auto_now_add = True)
    """If table name needs to be changed , do this """
    """class Meta:
        db_table = "my_blogs_tags"
    """    



# Representing a post
class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField()
    img_url = models.CharField(default = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS9XeELcp51xMR6GcbG86ssM_CLpG0QqiN9dw&usqp=CAU')
    pub_date = models.DateTimeField(auto_now_add=True)    
    author = models.ForeignKey(Author,on_delete = models.CASCADE)
    category = models.ForeignKey(Category, on_delete = models.CASCADE) # one Post to Many category
    tags = models.ManyToManyField(Tag) # many to many
    views_count = models.IntegerField(blank= True, help_text = "It will be updated dynamically and no need to set from admin.")
    likes_count = models.IntegerField(default = 0)

