from django.urls import path
from catalog.views import index, contacts, product

app_name = 'catalog'
urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('<int:pk>/product/', product, name='product'),
]
