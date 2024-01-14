from django.urls import path, include

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, SubTaskViewSet, TeamViewSet

router = DefaultRouter()
router.register(r'teams', TeamViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'subtasks', SubTaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
]