from django.shortcuts import render
from django.http import HttpResponse  
from .models import Post

### Add Dummy Post

# posts = [
#     {
#         'author': 'CoreyMS',
#         'title': 'Blog Post 1',
#         'content': 'First post content',
#         'date_posted': 'August 27, 2018'
#     },
#     {
#         'author': 'Jane Doe',
#         'title': 'Blog Post 2',
#         'content': 'Second post content',
#         'date_posted': 'August 28, 2018'
#     }
# ]
### Bolaji Alonge
posts = [
    {"author":"Bolaji Alonge", "title":"Post One", "content":"First post content", "date_posted":"Dec 24, 2025"},
    {"author":"DevOps Engineer", "title":"Post Two", "content":"Second post content", "date_posted":"Dec 24, 2025"},
]




### pass the Dictionary post as request into our templates so that we can use it
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})



# # Create your views here.
# def post_list(request):
#     return render(request, 'blog/post_list.html', {})

### OR Bolaji version
# def home(request):
#     context = {"posts": posts}
#     return render(request, "blog/post_list.html", context)


# ### corey
# def post_list(request):
#     return render(request, 'blog/home.html', {})

# def post_list(request):
#     return render(request, 'blog/about.html', {})  # you can now remove this i.e .......# from django.http import HttpResponse  

# ### corey
# def home(request):
#     return HttpResponse('<h1>Blog Home</h1>')

# def home(request): # to return http from our About
#     return HttpResponse('<h1>Blog About</h1>')

