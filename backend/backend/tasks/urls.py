from django.urls import path
from .views import TaskListCreateView, TaskUpdateDeleteView

urlpatterns = [
    path('tasks/', TaskListCreateView.as_view()),
    path('tasks/<int:id>/', TaskUpdateDeleteView.as_view()),
]