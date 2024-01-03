from django.shortcuts import render, redirect
from django.views import View
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator

from checkers_parser import settings
from .downloader import GitLabArtifactsDownloader

from .services import LogsService

superuser_required = method_decorator(staff_member_required(login_url='/admin/'))
downloader = GitLabArtifactsDownloader(
    gitlab_url=settings.GITLAB_URL,
    project_id=settings.PROJECT_ID,
    job_name=settings.JOB_NAME,
    access_token=settings.ACCESS_TOKEN
)


class LogsView(View):
    def get(self, request):
        try:
            logs_service = LogsService()
            absolute_path = f'/code/extracted_folder/quality_artifacts/{settings.RADON_CC_FILENAME}'
            formatted_data = logs_service.get_radon_formatted_data(absolute_path)
        except Exception as e:
            print(e)
            formatted_data = {}
        return render(
            request, 'radon_cc.html',
            {'formatted_data': formatted_data}
        )


class RadonMiView(View):
    def get(self, request):
        try:
            logs_service = LogsService()
            absolute_path = f'/code/extracted_folder/quality_artifacts/{settings.RADON_MI_FILENAME}'
            formatted_data = logs_service.mi_get_radon_formatted_data(absolute_path)
        except Exception as e:
            print(e)
            formatted_data = {}
        return render(
            request, 'radon_mi.html',
            {'formatted_data': formatted_data}
        )


class RuffView(View):
    def get(self, request):
        try:
            logs_service = LogsService()
            absolute_path = f'/code/extracted_folder/quality_artifacts/{settings.RUFF_FILENAME}'
            formatted_data = logs_service.get_ruff_formatted_data(absolute_path)
        except Exception as e:
            print(e)
            formatted_data = {}
        return render(
            request, 'ruff.html',
            {'formatted_data': formatted_data}
        )


class BanditView(View):
    def get(self, request):
        try:
            logs_service = LogsService()
            absolute_path = f'/code/extracted_folder/quality_artifacts/{settings.BANDIT_FILENAME}'
            formatted_data = logs_service.get_bandit_formatted_data(absolute_path)
        except Exception as e:
            print(e)
            formatted_data = {}
        return render(
            request, 'bandit.html',
            {'formatted_data': formatted_data}
        )


class GitlabView(View):
    def get(self, request):
        downloader.download_and_extract()
        return redirect("/")
