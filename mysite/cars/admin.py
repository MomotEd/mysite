from django.contrib import admin
from .models import Car, Comments, Catalog


admin.site.register(Comments)
admin.site.register(Catalog)


class CatalogAdmin(admin.ModelAdmin):
    change_list_template = 'cars/admin/add_catalog.html'

admin.site.register(Car, CatalogAdmin)