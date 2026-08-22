from django.contrib import admin
from .models import *

class categoryAdmin(admin.ModelAdmin):
    list_display = ("category_name", "slug", "description", "cat_image")
    
    prepopulated_fields = {'slug': ('category_name',)}

admin.site.register(category, categoryAdmin)