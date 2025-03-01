from django import forms
from index.models import Property, Query

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['title', 'description', 'address', 'type', 'price', 'size', 'rooms', 'condition', 'agent']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Описание'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите адрес'}),
            'type': forms.Select(attrs={'class': 'form-select'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Цена'}),
            'size': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Площадь (м²)'}),
            'rooms': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Количество комнат'}),
            'condition': forms.Select(attrs={'class': 'form-select'}),
            'agent': forms.Select(attrs={'class': 'form-select'}),
        }

class QueryForm(forms.ModelForm):
    class Meta:
        model = Query
        fields = ['query_date', 'status', 'message', 'user', 'property']
        widgets = {
            'query_date': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите дату'}),
            'status': forms.Select(attrs={'class':'form-select'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Сообщение'}),
            'user': forms.Select(attrs={'class': 'form-select'}),
            'property': forms.Select(attrs={'class': 'form-select'}),
        }