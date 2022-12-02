from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from wysiwyg_img.models import BaseImageModel


class HashTag(models.Model):
    title = models.CharField(max_length=200)

    @property
    def articles(self):
        return self.article_set.all()

    @property
    def related_articles(self):
        return self.article_set.all()[0:4]

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='article-images')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = HTMLField()
    description = models.TextField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    hash_tags = models.ManyToManyField(to=HashTag)
    # slug = models.SlugField()

    def __str__(self) -> str:
        return self.title


class PostImage(BaseImageModel):
    post = models.ForeignKey(Article, on_delete=models.CASCADE)


class Course(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='course-images')
    # slug  = models.SlugField()

    def __str__(self) -> str:
        return self.title

    @property
    def lessons(self):
        return self.lesson_set.all()


class Lesson(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='lesson-images')
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title


class QuizQuestions(models.Model):
    question = models.TextField()
    answer = models.TextField()
    course = models.ManyToManyField(Course)

    def __str__(self) -> str:
        return f'Quiz questions for {self.course.title}'
