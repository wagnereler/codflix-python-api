from django.contrib import admin

from django_api.category_app.models import Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'is_active']


admin.site.register(Category, CategoryAdmin)