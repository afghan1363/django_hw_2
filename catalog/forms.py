from django import forms

from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != 'is_current' and field_name != 'is_published':
                field.widget.attrs['class'] = 'form-control'
            #field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    danger_words = ('казино', 'криптовалюта', 'крипта', 'биржа',
                    'дешево', 'бесплатно', 'обман', 'полиция', 'радар',)

    class Meta:
        model = Product
        exclude = ('owner',)

    def clean_title(self):
        cleaned_data = self.cleaned_data['title']
        for word in self.danger_words:
            if word in cleaned_data.lower():
                raise forms.ValidationError('>|< ПОЛИЦИЯ УЖЕ ВЫЕХАЛА ЗА ТОБОЙ >|<')
        else:
            return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']
        for word in self.danger_words:
            if word in cleaned_data.lower():
                raise forms.ValidationError('>|< ПОЛИЦИЯ УЖЕ ВЫЕХАЛА ЗА ТОБОЙ >|<')
        else:
            return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Version
        fields = '__all__'
