from django.contrib import admin
from .models import EssentialsRequest, ContainmentZones, Districts

# Register your models here.

admin.site.register(EssentialsRequest)
admin.site.register(ContainmentZones)
admin.site.register(Districts)
