from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from projects_app.views import main_url, profile, ProjectsView, ProjectView, CreateProjectView, UpdateProjectView, DeleteProjectView

urlpatterns = [
    path('', main_url, name="base"),
    path("profile/<str:username>", profile, name="profile"),
    path("projects/", ProjectsView, name="projects"),
    path('project/<str:pk>', ProjectView, name='project'),
    path('create/', CreateProjectView, name='create-project'),
    path('update/<str:pk>', UpdateProjectView, name ='update-project'),
    path('dalete/<str:pk>', DeleteProjectView, name ='delete-project')
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)