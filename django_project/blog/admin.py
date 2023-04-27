from django.contrib import admin
from blog.models import Post, Author, Tag, Category, Comment


admin.site.register(Post)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Comment)

class AuthorAdmin(admin.ModelAdmin):
    pass


