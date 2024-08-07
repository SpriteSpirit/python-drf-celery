from rest_framework import viewsets, generics

from lms.models import Course, Lesson
from lms.serializers import CourseSerializer, LessonSerializer


# ViewSet для курса
class CourseViewSet(viewsets.ModelViewSet):
    """ """
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


# Generics для уроков
class LessonCreateAPIView(generics.CreateAPIView):
    """ Создание урока """
    serializer_class = LessonSerializer


class LessonListAPIView(generics.ListAPIView):
    """ Список уроков """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    """ Просмотр одного урока """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
