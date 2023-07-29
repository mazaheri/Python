from django.contrib import admin
from catalogue.models import Category, Brand, Product, ProductType, ProductAttribute, ProductImage


class ProductImageInline(admin.TabularInline):
    model = ProductImage


class ProductAttributesAdmin(admin.ModelAdmin):
    list_display = ['title', 'product_type', 'attribute_type']


class ProductAttributeInline(admin.TabularInline):
    model = ProductAttribute
    extra = 1


class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    inlines = [ProductAttributeInline]

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['upc', 'title', 'is_active', 'product_type', 'category', 'brand']
    list_filter = ['is_active']
    search_fields = ['upc', 'title', 'category__name','brand__name']
    actions = ['active_all']
    inlines = [ProductImageInline]

    def active_all(self, request, queryset):
        pass



admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductType, ProductTypeAdmin)
admin.site.register(ProductAttribute)