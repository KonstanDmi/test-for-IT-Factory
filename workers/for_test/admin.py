from django.contrib import admin
from .models import *
# Register your models here.


class WorkerAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone']
    search_fields = ['name']

class StoreAdmin(admin.ModelAdmin):
    list_display = ['title', 'latitude', 'longtitude']
    search_fields = ['title']
    filter_horizontal = ['workers']

class VisitAdmin(admin.ModelAdmin):
    list_display = ['date_of_visit', 'store', 'worker', 'latitude', 'longtitude']
    search_fields = ['store', 'worker']


admin.site.register(Worker, WorkerAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(Visit, VisitAdmin)