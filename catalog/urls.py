from django.urls import path
from django.views.decorators.cache import cache_page, never_cache
from catalog.views import (contacts, ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView,
                           ProductDeleteView, CategoryListView)

app_name = 'catalog'
urlpatterns = [
    path('', CategoryListView.as_view(), name='main_index'),
    path('product/<int:pk>', ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>/', cache_page(30)(ProductDetailView.as_view()), name='product'),
    path('product/create/', never_cache(ProductCreateView.as_view()), name='create_product'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='update_product'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='delete_product'),
    path('contacts/', contacts, name='contacts'),
]
