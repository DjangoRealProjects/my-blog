from django.urls import path
from . import views

# ### first URL pattern
# urlpatterns = [
#     path('', views.post_list, name='post_list'),
#     #path('app_name', views.post_list, name='view_name'),
# ]

## corey
urlpatterns = [
    path('', views.home, name='blog-home'), # be clear about how you name this name="blog-name"
    path('about/', views.about, name='blog-about'),
]
