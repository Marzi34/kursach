from django import forms
from .models import Query, Property

class QueryForm(forms.ModelForm):
    class Meta:
        model = Query
        fields = ['message']
        labels = {
            'message': 'Сообщение:'
        }
        widgets = {
            'message': forms.Textarea(attrs={'placeholder': 'Введите ваше сообщение', 'rows': 5}),
        }


class PropertyFilterForm(forms.Form):
    PROPERTY_TYPE_CHOICES = Property.PROPERTY_TYPE_CHOICES
    CONDITION_CHOICES = Property.CONDITION_CHOICES

    property_type = forms.ChoiceField(choices=[('', 'Все')] + PROPERTY_TYPE_CHOICES, required=False)
    condition = forms.ChoiceField(choices=[('', 'Все')] + CONDITION_CHOICES, required=False)
    min_price = forms.DecimalField(required=False, min_value=0, decimal_places=2)
    max_price = forms.DecimalField(required=False, min_value=0, decimal_places=2)
    min_size = forms.IntegerField(required=False, min_value=0)
    max_size = forms.IntegerField(required=False, min_value=0)
    min_rooms = forms.IntegerField(required=False, min_value=0)
    max_rooms = forms.IntegerField(required=False, min_value=0)

    labels = {
        'property_type': 'Тип:',
        'condition': 'Состояние:',
        'min_price': 'Минимальная цена:',
        'max_price': 'Максимальная цена:',
        'min_size': 'Минимальные размер:',
        'max_size': 'Максимальный размер:',
        'min_rooms': 'Минимально комнат:',
        'max_rooms': 'Максимально комнат:',
    }