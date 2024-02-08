from .models import GitlabProject


class ProjectsRepository:
    def get_all_projects(self) -> list[GitlabProject]:
        return GitlabProject.objects.all()

    def get_project_by_id(self, project_id: int) -> GitlabProject:
        return GitlabProject.objects.get(id=project_id)
