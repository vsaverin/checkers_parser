from django.shortcuts import render, redirect
from django.views import View
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator

from checkers_parser import settings
from .downloader import GitLabArtifactsDownloader

from .services import LogsService, ProjectsService

superuser_required = method_decorator(staff_member_required(login_url="/admin/"))
logs_service = LogsService()
projects_service = ProjectsService()
downloader = GitLabArtifactsDownloader(
    gitlab_url=settings.GITLAB_URL,
    project_id=settings.PROJECT_ID,
    job_name=settings.JOB_NAME,
    access_token=settings.ACCESS_TOKEN,
)


class LogsView(View):
    @superuser_required
    def get(self, request):
        try:
            absolute_path = (
                f"{settings.BASE_ARTIFACTS_PATH}{settings.RADON_CC_FILENAME}"
            )
            formatted_data = logs_service.get_radon_formatted_data(absolute_path)
        except Exception as e:
            print(e)
            formatted_data = {}
        return render(request, "radon_cc.html", {"formatted_data": formatted_data})


class RadonMiView(View):
    @superuser_required
    def get(self, request):
        try:
            absolute_path = (
                f"{settings.BASE_ARTIFACTS_PATH}{settings.RADON_MI_FILENAME}"
            )
            formatted_data = logs_service.mi_get_radon_formatted_data(absolute_path)
        except Exception as e:
            print(e)
            formatted_data = {}
        return render(request, "radon_mi.html", {"formatted_data": formatted_data})


class RuffView(View):
    @superuser_required
    def get(self, request):
        try:
            absolute_path = f"{settings.BASE_ARTIFACTS_PATH}{settings.RUFF_FILENAME}"
            formatted_data = logs_service.get_ruff_formatted_data(absolute_path)
        except Exception as e:
            print(e)
            formatted_data = {}
        return render(request, "ruff.html", {"formatted_data": formatted_data})


class BanditView(View):
    @superuser_required
    def get(self, request):
        try:
            absolute_path = f"{settings.BASE_ARTIFACTS_PATH}{settings.BANDIT_FILENAME}"
            formatted_data = logs_service.get_bandit_formatted_data(absolute_path)
        except Exception as e:
            print(e)
            formatted_data = {}
        return render(request, "bandit.html", {"formatted_data": formatted_data})


class GitlabView(View):
    @superuser_required
    def get(self, request):
        downloader.download_and_extract()
        return redirect("/")


class DashboardView(View):
    @superuser_required
    def get(self, request):
        projects = projects_service.get_all_projects()
        return render(request, "dashboard.html", {"projects": projects})


class DisplayProjectView(View):
    @superuser_required
    def get(self, request, project_id: int):
        project = projects_service.get_project_data(project_id)
        project_artifacts = logs_service.get_all_artifacts_by_project_id(
            project.project_id
        )
        return render(
            request,
            "project.html",
            {
                "project": project,
                "project_artifacts": project_artifacts,
            },
        )
