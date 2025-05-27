from django.contrib import admin
from .models import *

class NotogriInline(admin.StackedInline):
    model = Notogri
    extra = 1

class TogriAdmin(admin.ModelAdmin):
    inlines = [NotogriInline]

admin.site.register(Togri, TogriAdmin)
admin.site.register(Notogri)
