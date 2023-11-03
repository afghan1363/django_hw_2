from django.shortcuts import render

from catalog.models import Product


# Create your views here.
def index(request):
    product_list = Product.objects.all()
    context = {
        'product_list': product_list,
        'title': 'Магазин хороших прог'
    }
    return render(request, 'catalog/index.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f"""
Имя: {name},
Телефон: {phone},
Сообщение:'{message}'""")
    return render(request, 'catalog/contact.html')


def product(request, pk):
    product_item = Product.objects.get(pk=pk)
    products = Product.objects.filter(id=pk)
    context = {
        'product_list': products,
        'title': f'Описание проги {product_item.title}'
    }
    return render(request, 'catalog/product.html', context)
