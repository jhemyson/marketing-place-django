from django.contrib import admin
from .models import Category, Product, ProductQuestion, ProductAnswer


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}
    list_filter = ['hidden']
    list_display = ('id', 'name', 'parent', 'hidden')


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}
    list_filter = ['status']
    list_display = ('id', 'name', 'short_description', 'status')


class ProductAnswerInline(admin.StackedInline):
    model = ProductAnswer
    can_delete = False


class ProductQuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'question', 'status')

    inlines = (ProductAnswerInline,)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductQuestion, ProductQuestionAdmin)




