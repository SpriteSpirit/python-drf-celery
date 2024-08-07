from lms.apps import LmsConfig
from rest_framework.routers import DefaultRouter
from django.urls import path

from lms.views import CourseViewSet
from lms.views import LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView

app_name = LmsConfig.name

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')

urlpatterns = [
    path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson-create'),
    path('lesson/', LessonListAPIView.as_view(), name='lesson-list'),
    path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson-get'),
] + router.urls
