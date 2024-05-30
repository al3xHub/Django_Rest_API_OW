from django.urls import include, path
from .views import TaskView, TaskViewSet, CustomAuthToken
from rest_framework import routers
from rest_framework.authtoken import views


router = routers.DefaultRouter()
router.register(r'tareas', TaskViewSet)

urlpatterns = [
    path('tasks/', TaskView.as_view(), name='task_list'),
    path('tasks/<int:pk>', TaskView.as_view(), name='task_detail'),
    path('', include(router.urls)),
    path('api-token-auth/', CustomAuthToken.as_view() ),
]
