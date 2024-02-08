# Generated by Django 4.1 on 2024-01-06 14:17

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="GitlabProject",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("project_name", models.CharField(max_length=128)),
                ("project_id", models.CharField(max_length=128)),
                ("analysis_job_name", models.CharField(max_length=128)),
                ("bandit_filename", models.CharField(max_length=128)),
                ("ruff_filename", models.CharField(max_length=128)),
                ("radon_mi_filename", models.CharField(max_length=128)),
                ("radon_cc_filename", models.CharField(max_length=128)),
            ],
        ),
    ]