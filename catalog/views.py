from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from catalog.models import Product


# Create your views here.
class ProductListView(ListView):
    model = Product
    template_name = 'catalog/index.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product.html'


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f"""
Имя: {name},
Телефон: {phone},
Сообщение:'{message}'""")
    return render(request, 'catalog/contacts.html')


# def product(request, pk):
#     product_item = Product.objects.get(pk=pk)
#     products = Product.objects.filter(id=pk)
#     context = {
#         'product_list': products,
#         'title': f'Описание проги {product_item.title}'
#     }
#     return render(request, 'catalog/product.html', context)
