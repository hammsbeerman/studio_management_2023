from django.contrib import admin

# Register your models here.

from .models import KruegerJobDetail

class KruegerJobDetailAdmin(admin.ModelAdmin):
    readonly_fields = ["qty_of_sheets"]

admin.site.register(KruegerJobDetail, KruegerJobDetailAdmin)