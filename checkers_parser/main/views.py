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
    access_token=settings.ACCESS_TOKEN,
)


class GitlabView(View):
    @superuser_required
    def get(self, request, project_id: int):
        project_data = projects_service.get_project_data(project_id)
        downloader.download_and_extract(
            project_id=project_id,
            job_name=project_data.analysis_job_name
        )
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
