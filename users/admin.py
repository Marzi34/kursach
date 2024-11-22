from django.contrib import admin
from .models import CustomUser, Agent, Client

admin.site.register(CustomUser)
admin.site.register(Agent)
admin.site.register(Client)

