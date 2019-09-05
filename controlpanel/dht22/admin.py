from django.contrib import admin
from .models import Dht22, Data

admin.site.register(Dht22)
admin.site.register(Data)

class DataInline(admin.TabularInline):
    model = Data

class Dht22Admin(admin.ModelAdmin):
    inlines = [
        DataInline,
    ]
