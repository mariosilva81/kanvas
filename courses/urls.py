from django.urls import path
from .views import CourseView, CourseDetailView
from students_courses.views import StudentDetailView
from contents.views import ContentView, ContentDetailView

urlpatterns = [
    path("courses/", CourseView.as_view()),
    path("courses/<uuid:course_id>/", CourseDetailView.as_view()),
    path("courses/<uuid:course_id>/students/", StudentDetailView.as_view()),
    path("courses/<uuid:course_id>/contents/", ContentView.as_view()),
    path("courses/<uuid:course_id>/contents/<uuid:content_id>/", ContentDetailView.as_view()),
]
