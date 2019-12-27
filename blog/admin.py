from django.contrib import admin
from .models import Post


# Customize the way the admin panel looks
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')  # displays the properties mentioned in the tuple
    list_filter = ('created_on',) 
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


# Register your models here.
admin.site.register(Post, PostAdmin)

