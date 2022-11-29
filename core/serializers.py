from .models import HashTag, Lesson, Article, Course
from rest_framework import serializers


class HashTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = HashTag
        field = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        field = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        field = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        field = '__all__'
