from django import forms
from webapp.models import CATEGORY_CHOICES


class ProductForm(forms.Form):
    name = forms.CharField(max_length=100, label='Название', required=True)
    description = forms.CharField(max_length=2000, label='Описание', required=False,
                           widget=forms.Textarea(attrs={'rows': 8, 'cols': 15}))
    category = forms.ChoiceField(label='Категория', required=True, choices=CATEGORY_CHOICES)
    remain = forms.IntegerField(min_value=0, label='Остаток')
    price = forms.DecimalField(max_digits=7, decimal_places=2, label='Цена')


class SearchForm(forms.Form):
    pattern = forms.CharField(max_length=100, required=True, label='',widget=forms.TextInput(attrs={
        'placeholder': 'Введите имя'}))