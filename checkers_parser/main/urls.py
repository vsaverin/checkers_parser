from django.urls import path

from .views import LogsView, RadonMiView, RuffView, BanditView, GitlabView

urlpatterns = [
    path("", LogsView.as_view()),
    path("radon/mi/", RadonMiView.as_view()),
    path("ruff/", RuffView.as_view()),
    path("bandit/", BanditView.as_view()),
    path("gitlab-data/update/", GitlabView.as_view()),
]
