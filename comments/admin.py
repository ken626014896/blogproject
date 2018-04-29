from django.contrib import admin

# Register your models here.
from comments.models import Comment



class  CommentAdmin(admin.ModelAdmin):

    list_display = ["name",'email','url','text']


admin.site.register(Comment,CommentAdmin)
