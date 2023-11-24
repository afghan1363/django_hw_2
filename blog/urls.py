from django.urls import path
from blog.views import BlogCreateView, BlogListView, BlogDetailView, BlogUpdateView, BlogDeleteView
from django.views.decorators.cache import never_cache

app_name = 'blog'

urlpatterns = [
    path('', BlogListView.as_view(), name='list'),
    path('create/', never_cache(BlogCreateView.as_view()), name='create'),
    path('view/<slug>/', BlogDetailView.as_view(), name='view'),
    path('update/<slug>/', BlogUpdateView.as_view(), name='update'),
    path('delete/<slug>/', BlogDeleteView.as_view(), name='delete'),
]
