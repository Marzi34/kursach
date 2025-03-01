from django.urls import path
from .views import *

urlpatterns = [
    path('', admin_panel, name='admin_panel'),
    path('houses_list/', houses_list, name='houses_list'),
    path('detail_houses/<int:property_id>/', property_edit, name='property_edit'),
    path('remove/<int:property_id>/', remove_from_list, name='remove_btn'),
    path('creation_form/', creation_form, name='creation_form'),
    path('queries_list/', queries_list, name='queries_list'),
    path('query_edit/<int:query_id>/', query_edit, name='query_edit'),
    path('remove/<int:query_id>/', remove_query, name='removeq_btn'),
    path('creation_query', creation_query, name='creation_query'),
]