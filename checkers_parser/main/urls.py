from django.urls import path

from .views import (
    GitlabView,
    DashboardView,
    DisplayProjectView,
)

urlpatterns = [
    path("", DashboardView.as_view()),
    path("projects/<int:project_id>/", DisplayProjectView.as_view()),
    path("gitlab-data/update/<int:project_id>/", GitlabView.as_view()),
]
