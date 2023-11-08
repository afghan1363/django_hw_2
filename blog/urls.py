from django.urls import path
from blog.views import BlogCreateView, BlogListView, BlogDetailView, BlogUpdateView, BlogDeleteView

app_name = 'blog'
urlpatterns = [
    path('create/', BlogCreateView.as_view(), name='create'),
    path('', BlogListView.as_view(), name='list'),
    path('view/<slug:slug>/', BlogDetailView.as_view(), name='view'),
    path('update/<slug:slug>/', BlogUpdateView.as_view(), name='update'),
    path('delete/<slug:slug>/', BlogDeleteView.as_view(), name='delete'),
]
