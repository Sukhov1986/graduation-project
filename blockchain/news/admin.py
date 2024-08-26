from django.contrib import admin
from .models import News, Comments
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

class NewsAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())



class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm
    list_display = ('title', 'published_date', 'total_likes')
    search_fields = ('title', 'content',)
    list_filter = ('published_date', )

class CommentsAdmin(admin.ModelAdmin):
    list_display = ('owner', 'news', 'comment', 'created')

admin.site.register(News, NewsAdmin)
admin.site.register(Comments, CommentsAdmin)

