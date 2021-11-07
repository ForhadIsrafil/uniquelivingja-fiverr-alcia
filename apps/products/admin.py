from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import *


class ProductResource(resources.ModelResource):
    class Meta:
        model = Product


class ProductAdmin(ImportExportModelAdmin):
    resource_class = ProductResource
    list_display = ['name', 'brand', 'sku', 'price', 'category_name', ]
    search_fields = ["name", 'brand', 'sku', ]
    list_editable = ['price', 'category_name',]


admin.site.register(Product, ProductAdmin)
