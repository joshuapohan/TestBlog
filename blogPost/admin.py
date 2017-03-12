from django.contrib import admin
from blogPost.models import WritePost

class PostAdmin(admin.ModelAdmin):
    list_display = ('date_posted','blog_title','blog_post','post_author')
    search_fields =('post_author')
