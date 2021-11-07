from django.urls import path
from .views import projects, project, make_project, update_project, delete_project

urlpatterns = [
    path('', projects, name='projects'),
    path('project/<str:pk>/', project, name='project'),
    path('make-project/', make_project, name='make_project'),
    path('update-project/<str:pk>/', update_project, name='update_project'),
    path('delete-project/<str:pk>/', delete_project, name='delete_project'),
]