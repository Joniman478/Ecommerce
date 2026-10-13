from django.contrib import admin
from .models import *
# Register your models here.

class prodcutAdmin(admin.ModelAdmin):
    list_display = ("product_name", "slug", "price" , "stock", "is_available", "category", "created_date", "modified_date")
    prepopulated_fields = {"slug": ("product_name",)}
    ordering = ("-created_date",)

class variationAdmin(admin.ModelAdmin):
    list_display = ("product" , "variation_category", "variation_value", "created_date", "is_active")
    list_editable = ("is_active",)
    list_filter =  ("product" , "variation_category", "variation_value", "created_date", "is_active")

admin.site.register(Product, prodcutAdmin)
admin.site.register(Variation, variationAdmin)