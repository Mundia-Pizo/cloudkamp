from django.contrib import admin
from .models import HashTag, Article, Course, Lesson, PostImage


from django.contrib import admin

from wysiwyg_img.admin import ImageInline


class PostImageInline(ImageInline):
    model = PostImage


class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        PostImageInline,
    ]


admin.site.register(Article, ArticleAdmin)

admin.site.register(HashTag)
# admin.site.register(Article)
admin.site.register(Course)
admin.site.register(Lesson)
