from django.contrib import admin
from .models import CryptoPerson

@admin.register(CryptoPerson)
class CryptoPersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'published_date')

# Register your models here.
