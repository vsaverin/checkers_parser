import requests
import zipfile
import os


class GitLabArtifactsDownloader:
    def __init__(self, gitlab_url, access_token):
        self.gitlab_url = gitlab_url
        self.access_token = access_token
        self.download_path_default = "artifacts.zip"
        self.extract_to_folder_default = "extracted_folder"

    def download_artifacts(self, project_id: int, job_name: str) -> bool:
        job_url = (
            f"{self.gitlab_url}/api/v4/projects/"
            f"{project_id}/jobs"
            f"?scope=success&per_page=1&name={job_name}"
        )
        headers = {"Private-Token": self.access_token}
        response = requests.get(job_url, headers=headers, timeout=30)

        if response.status_code == 200:
            job_id = response.json()[0]["id"]
            artifacts_url = (
                f"{self.gitlab_url}/api/v4/projects/"
                f"{project_id}/jobs/{job_id}/artifacts"
            )
            artifacts_response = requests.get(
                artifacts_url, headers=headers, allow_redirects=True, timeout=30
            )

            if artifacts_response.status_code == 200:
                with open(
                    f"{project_id}/{job_name}/{self.download_path_default}", "wb"
                ) as file:
                    file.write(artifacts_response.content)
                    print("Artifacts downloaded successfully.")
                    return True
            else:
                print("Failed to fetch artifacts.")
        else:
            print("Failed to fetch job information.")
        return False

    def extract_artifacts(self, project_id: int, job_name: str):
        with zipfile.ZipFile(
            f"{project_id}/{job_name}/{self.download_path_default}", "r"
        ) as zip_ref:
            zip_ref.extractall(f"{project_id}/{job_name}/{self.extract_to_folder_default}")
            print("Extraction completed successfully.")

    def cleanup(self, project_id: int, job_name: str):
        if os.path.exists(f"{project_id}/{job_name}/{self.download_path_default}"):
            os.remove(f"{project_id}/{job_name}/{self.download_path_default}")
            print(f"Removed {project_id}/{job_name}/{self.download_path_default}")

    def download_and_extract(self, project_id: int, job_name: str):
        if self.download_artifacts(project_id=project_id, job_name=job_name):
            self.extract_artifacts(project_id=project_id, job_name=job_name)
            self.cleanup(project_id=project_id, job_name=job_name)
