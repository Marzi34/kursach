from django.http import HttpResponse, HttpResponseForbidden
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from index.models import Property, PropertyImage, Query
from users.models import CustomUser
from .forms import *


def admin_panel(request):
    if not request.user.is_staff:
        return HttpResponseForbidden("У вас нет прав к этой странице")
    return render(request, 'admin_panel.html')

def houses_list(request):
    if not request.user.is_staff:
        return HttpResponseForbidden("У вас нет прав к этой странице")
    houses = Property.objects.all()
    return render(request, 'houses_list.html', {'houses': houses})

def detail_houses(request, property_id):
    if not request.user.is_staff:
        return HttpResponseForbidden("У вас нет прав к этой странице")
    print(property_id)
    property = get_object_or_404(Property, id=property_id)
    images = PropertyImage.objects.filter(property=property)
    return render(request, 'house_detail.html', {'property': property, 'images': images})

def creation_form(request):
    if not request.user.is_staff:
        return HttpResponseForbidden("У вас нет прав к этой странице")
    if request.method == "POST":
        form = PropertyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('houses_list/')
    else:
        form = PropertyForm()
    return render(request, 'create_house_form.html', {'form': form})


def property_edit(request, property_id):
    if not request.user.is_staff:
        return HttpResponseForbidden("У вас нет прав к этой странице")
    property_instance = get_object_or_404(Property, id=property_id)

    if request.method == "POST":
        form = PropertyForm(request.POST, instance=property_instance)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = PropertyForm(instance=property_instance)

    return render(request, 'house_detail.html', {'form': form, 'property': property_instance})

def remove_from_list(request, property_id):
    if not request.user.is_staff:
        return HttpResponseForbidden("У вас нет прав к этой странице")
    Property.objects.filter(id=property_id).delete()

def queries_list(request):
    if not request.user.is_staff:
        return HttpResponseForbidden("У вас нет прав к этой странице")
    queries = Query.objects.all()
    return render(request, 'queries_list.html', {'queries': queries})

def query_edit(request, query_id):
    if not request.user.is_staff:
        return HttpResponseForbidden("У вас нет прав к этой странице")
    query_instance = get_object_or_404(Query, id=query_id)

    if request.method == "POST":
        form = QueryForm(request.POST, instance=query_instance)
        if form.is_valid():
            form.save()
            return redirect('query_list')
    else:
        form = QueryForm(instance=query_instance)

    return render(request, 'query_edit.html', {'form': form, 'query': query_instance})

def remove_query(request, query_id):
    if not request.user.is_staff:
        return HttpResponseForbidden("У вас нет прав к этой странице")
    Query.objects.filter(id=query_id).delete()
    return redirect('query_list')

def creation_query(request):
    if not request.user.is_staff:
        return HttpResponseForbidden("У вас нет прав к этой странице")
    if request.method == "POST":
        form = QueryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('queries_list/')
    else:
        form = QueryForm()
    return render(request, 'create_query_form.html', {'form': form})