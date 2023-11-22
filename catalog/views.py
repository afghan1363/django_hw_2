from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from catalog.models import Product, Version
from catalog.forms import ProductForm, VersionForm, ModeratorProductForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import Http404


# Create your views here.
class ProductListView(LoginRequiredMixin, ListView):
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

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset()
        # queryset = queryset.filter(owner_id=self.kwargs.get('pk'), )
        if not self.request.user.is_staff:
            queryset = queryset.filter(owner=self.request.user)
        # queryset = queryset.filter(owner=self.request.user)
        # elif self.object.owner == self.request.user:
        #     queryset = queryset.filter(owner=self.request.user) + queryset.filter(is_published=True)
        # else:
        #     queryset = queryset
        return queryset


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'catalog/product.html'
    extra_context = {
        'title': 'SkyStore'
    }


class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    login_url = "users:login"
    permission_required = 'catalog.add_product'

    # success_url = reverse_lazy('catalog:index')
    def get_success_url(self):
        return reverse_lazy('catalog:product', args=[self.object.pk])

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ModeratorProductForm
    login_url = "users:login"
   # permission_required = 'catalog.change_product'

    # success_url = reverse_lazy('catalog:index')
    def get_success_url(self):
        return reverse_lazy('catalog:product', args=[self.object.pk])

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if (self.request.user != self.object.owner and not self.request.user.is_staff
                and not self.request.user.is_superuser and self.request.user.has_perm('catalog.set_published')):
            raise Http404
        else:
            return self.object

    def get_form_class(self):
        """Return the form class to use."""
        if not self.request.user.is_staff:
            self.form_class = ProductForm
        else:
            self.form_class = ModeratorProductForm
        return self.form_class

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


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:index')
    login_url = "users:login"
    permission_required = 'catalog.delete_product'

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
