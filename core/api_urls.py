from django.urls import path
from .views import HomePage, PostDetailView, CategoryView, Posts, CourseListView, CourseDetailView, LessonDetailView

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('posts/', Posts.as_view(), name='posts'),
    path('courses/', CourseListView.as_view(), name='courses'),
    path('post/<int:pk>/detail', PostDetailView.as_view(), name='post-detail'),
    path('lesson/<int:pk>/detail', LessonDetailView.as_view(), name='lesson-detail'),
    path('course/<int:pk>/detail', CourseDetailView.as_view(), name='course-detail'),
    path('category/<int:pk>/detail',
         CategoryView.as_view(), name='category-detail'),


]
