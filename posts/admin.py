from django.contrib.auth import get_user_model
from django.contrib import admin

# Register your models here.
from .models import Post, Link

User = get_user_model()

class LinkInline(admin.StackedInline):
    model = Link
    extra = 0
    # readonly_fields = ['url',]
    fields = ['url']

class PostAdmin(admin.ModelAdmin):
    inlines = [LinkInline]
    list_display = ['title', 'description']
    readonly_fields = ['date',]
    raw_id_fields = ['author']

admin.site.register(Post, PostAdmin)