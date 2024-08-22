from django.contrib import admin
from .models import Profile, Message

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'email', 'username', 'created')
    search_fields = ('name', 'username',)
    list_filter = ('created',)

class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'recipient', 'content', 'is_read', 'created')
    search_fields = ('sender', 'recipient',)
    list_filter = ('created',)

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Message, MessageAdmin)
