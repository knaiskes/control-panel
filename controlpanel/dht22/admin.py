from django.contrib import admin
from .models import Dht22, Record

admin.site.register(Dht22)
admin.site.register(Record)

class RecordInline(admin.TabularInline):
    model = Record

class Dht22Admin(admin.ModelAdmin):
    inlines = [
        RecordInline,
    ]
