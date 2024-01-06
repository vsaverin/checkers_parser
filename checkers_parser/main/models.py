from django.db import models


class GitlabProject(models.Model):
    project_name = models.CharField(max_length=128)
    project_id = models.CharField(max_length=128)
    analysis_job_name = models.CharField(max_length=128)

    bandit_filename = models.CharField(max_length=128)
    ruff_filename = models.CharField(max_length=128)
    radon_mi_filename = models.CharField(max_length=128)
    radon_cc_filename = models.CharField(max_length=128)
