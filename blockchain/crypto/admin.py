from django.contrib import admin
from .models import Crypto, Category

class CryptoAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_name', 'last_updated')
    search_fields = ('name', 'short_name',)
    list_filter = ('categories',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Crypto, CryptoAdmin)
admin.site.register(Category, CategoryAdmin)
