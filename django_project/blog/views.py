from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from blog.models import Post
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator


from django import template
from django.conf import settings

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

    print('page_obj = ' , posts.number,'page_number = ', page_number, 'count ', paginator.num_pages)

    data_dict = { 'posts' : posts }
    return render(request, 'index.html', data_dict)
    

# details of the blog / post
def get_post_details(request, post_id):
    try:
        post = Post.objects.get(pk = post_id)
    except ObjectDoesNotExist as e:
        return render(request, 'post_details.html', { 'error_message' : str(e)})
    
    return render(request, 'post_details.html', { 'post' : post})

def get_blogs(request):
    return redirect('/')

# Test method
def date_today(request):
    today = datetime.now()
    html = "<html><body><h3>Current date and time: {0}</h3></body></html>".format(today)
    return HttpResponse(html)