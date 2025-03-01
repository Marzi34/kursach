from django.http import HttpResponse
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from index.models import Property, PropertyImage
from users.models import Client
from .forms import QueryForm
from .forms import PropertyFilterForm



def index(request):
    return render(request, 'index/index.html')

def catalog(request):
    houses = Property.objects.all()
    return render(request, 'index/catalog.html', {'houses': houses})

def detail_view(request, property_id):
    property = get_object_or_404(Property, id=property_id)
    images = PropertyImage.objects.all()
    price_f_metr = property.price // property.size
    return render(request, 'index/detail.html', {'property': property, 'images': images, 'price_f_metr': price_f_metr})

def submit_form(request, property_id):
    property_instance = get_object_or_404(Property, id=property_id)
    user_instance = get_object_or_404(Client, user=request.user.id)

    if request.method == "POST":
        form = QueryForm(request.POST)
        if form.is_valid():
            query = form.save(commit=False)
            query.user = user_instance
            query.property = property_instance
            query.query_date = timezone.now().date()
            query.status = "Рассматриваемый"
            query.save()
            return redirect('detail_view', property_id=property_instance.id)
    else:
        form = QueryForm()

    return render(request, 'index/submit_form.html', {'form': form, 'property': property_instance})


def property_list(request):
    form = PropertyFilterForm(request.GET or None)
    properties = Property.objects.all()

    if form.is_valid():
        if form.cleaned_data['property_type']:
            properties = properties.filter(type=form.cleaned_data['property_type'])
        if form.cleaned_data['condition']:
            properties = properties.filter(condition=form.cleaned_data['condition'])
        if form.cleaned_data['min_price']:
            properties = properties.filter(price__gte=form.cleaned_data['min_price'])
        if form.cleaned_data['max_price']:
            properties = properties.filter(price__lte=form.cleaned_data['max_price'])
        if form.cleaned_data['min_size']:
            properties = properties.filter(size__gte=form.cleaned_data['min_size'])
        if form.cleaned_data['max_size']:
            properties = properties.filter(size__lte=form.cleaned_data['max_size'])
        if form.cleaned_data['min_rooms']:
            properties = properties.filter(rooms__gte=form.cleaned_data['min_rooms'])
        if form.cleaned_data['max_rooms']:
            properties = properties.filter(rooms__lte=form.cleaned_data['max_rooms'])

    return render(request, 'index/catalog.html', {'form': form, 'properties': properties})