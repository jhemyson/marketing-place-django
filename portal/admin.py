from django.contrib import admin
from .models import Category


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}
    list_filter = ['hidden']
    list_display = ('id', 'name', 'parent', 'hidden')


admin.site.register(Category, CategoryAdmin)


