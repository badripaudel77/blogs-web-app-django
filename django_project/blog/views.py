from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
from blog.models import Post, Comment
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator


from django import template

ITEM_PER_PAGE = 6

"""
 This lists all the posts, probably implement pagination here later on
"""
def index(request):
    post_lists = Post.objects.all().order_by('-pub_date')
    # Create paginator object with posts and pass how many posts you want per page
    paginator = Paginator(post_lists, ITEM_PER_PAGE)
    page_number = request.GET.get('page')
    if page_number is None:
        page_number = 1
    # Use the get_page() method to retrieve the items for the current page, page_obj and paginator have  numberous methods and fields required for pagionation.
    posts = paginator.get_page(page_number)
    data_dict = { 'posts' : posts }
    return render(request, 'index.html', data_dict)
    

# details of the blog / post
def get_post_details(request, post_id):
    try:
        post = Post.objects.get(pk = post_id)
        comments = Comment.objects.all().filter(post_id = post.id).order_by('-created_on')[:3]
        post.views_count = post.views_count + 1
        post.save()
        related_posts = get_related_posts(post.category)
    except ObjectDoesNotExist as e:
        return render(request, 'post_details.html', { 'error_message' : str(e)})
    return render(request, 'post_details.html', { 'post' : post, 'comments': comments, 'related_posts' : related_posts })

#  post the comment 
def post_comment(request,post_id):
    if request.method == 'POST':
        posted_by = request.POST['name']
        comment_desc = request.POST['comment']
        post = Post.objects.get(pk = post_id)
        # comment.post = post 
        comment = Comment(posted_by = posted_by, comment_desc = comment_desc, post = post)
        comment.save()
        # redirect to the same page
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        # return get_post_details(request, post_id)
   

def get_blogs(request):
    return redirect('/')

# get all the posts of the author
def all_posts_of_author(request, author_id):
    author_posts = Post.objects.all().filter(author_id = author_id).order_by('-pub_date')
    paginator = Paginator(author_posts, ITEM_PER_PAGE)
    page_number = request.GET.get('page')

    if page_number is None:
        page_number = 1
    posts = paginator.get_page(page_number)

    return render(request, 'author_posts.html', { 'posts' : posts, 'author' : posts[0].author.name })

def get_related_posts(category):
    return Post.objects.all().filter(category = category ).order_by('-pub_date')[:3]


# Test method
def date_today(request):
    today = datetime.now()
    html = "<html><body><h3>Current date and time: {0}</h3></body></html>".format(today)
    return HttpResponse(html)