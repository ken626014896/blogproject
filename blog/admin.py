from django.contrib import admin

# Register your models here.
from blog.models import Tag,Post,Category


class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)


class PostAdmin(admin.ModelAdmin):

    list_display = ("title","body","created_time","modified_time","excerpt","category","author",)




admin.site.register(Tag,TagAdmin)

admin.site.register(Category,CategoryAdmin)

admin.site.register(Post,PostAdmin)