from django.contrib import admin
from .models import Property, Query, PropertyImage

admin.site.register(Property)
admin.site.register(Query)
admin.site.register(PropertyImage)