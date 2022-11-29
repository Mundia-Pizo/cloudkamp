from django.contrib import admin


from .models import HashTag, Article, Course, Lesson
admin.site.register(HashTag)
admin.site.register(Article)
admin.site.register(Course)
admin.site.register(Lesson)
