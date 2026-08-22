from django.contrib import admin
from .models import *
# Register your models here.

class prodcutAdmin(admin.ModelAdmin):
    list_display = ("product_name", "slug", "price" , "stock", "is_available", "category", "created_date", "modified_date")
    prepopulated_fields = {"slug": ("product_name",)}
    ordering = ("-created_date",)

admin.site.register(Product, prodcutAdmin)