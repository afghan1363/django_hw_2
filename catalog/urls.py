from django.urls import path
from catalog.views import contacts, product, ProductListView, ProductDetailView

app_name = 'catalog'
urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
]
