from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from catalog.models import Product, Version
from catalog.forms import ProductForm, VersionForm


# Create your views here.
class ProductListView(ListView):
    model = Product
    template_name = 'catalog/index.html'
    extra_context = {
        'title': 'SkyStore - Магазин и Блог, Блогазин, Магалог'
    }

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        for product in context['object_list']:
            active_version = product.version_set.filter(is_current=True).first()
            if active_version:
                product.active_version_number = active_version.version_number
                product.active_title = active_version.title
            else:
                product.active_version_number = ''
                product.active_title = 'Доступна тестовая версия'

        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product.html'
    extra_context = {
        'title': 'SkyStore'
    }


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm

    # success_url = reverse_lazy('catalog:index')
    def get_success_url(self):
        return reverse_lazy('catalog:product', args=[self.object.pk])


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm

    # success_url = reverse_lazy('catalog:index')
    def get_success_url(self):
        return reverse_lazy('catalog:product', args=[self.object.pk])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data


    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:index')

    def get_context_data(self, **kwargs):
        """Переопределение метода """
        context_data = super().get_context_data(**kwargs)
        product_item = Product.objects.get(pk=self.kwargs.get('pk'))
        context_data['product_pk'] = product_item.pk
        context_data['title'] = f'Удаление программы {product_item.title}'
        return context_data


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
