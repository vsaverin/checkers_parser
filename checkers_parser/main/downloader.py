import requests
import zipfile
import os


class GitLabArtifactsDownloader:
    def __init__(self, gitlab_url, project_id, job_name, access_token):
        self.gitlab_url = gitlab_url
        self.project_id = project_id
        self.job_name = job_name
        self.access_token = access_token
        self.download_path = "artifacts.zip"
        self.extract_to_folder = "extracted_folder"

    def download_artifacts(self):
        job_url = (
            f"{self.gitlab_url}/api/v4/projects/"
            f"{self.project_id}/jobs"
            f"?scope=success&per_page=1&name={self.job_name}"
        )
        headers = {"Private-Token": self.access_token}
        response = requests.get(job_url, headers=headers, timeout=30)

        if response.status_code == 200:
            job_id = response.json()[0]["id"]
            artifacts_url = (
                f"{self.gitlab_url}/api/v4/projects/"
                f"{self.project_id}/jobs/{job_id}/artifacts"
            )
            artifacts_response = requests.get(
                artifacts_url, headers=headers,
                allow_redirects=True, timeout=30
            )

            if artifacts_response.status_code == 200:
                with open(self.download_path, "wb") as file:
                    file.write(artifacts_response.content)
                    print("Artifacts downloaded successfully.")
                    return True
            else:
                print("Failed to fetch artifacts.")
        else:
            print("Failed to fetch job information.")
        return False

    def extract_artifacts(self):
        with zipfile.ZipFile(self.download_path, "r") as zip_ref:
            zip_ref.extractall(self.extract_to_folder)
            print("Extraction completed successfully.")

    def cleanup(self):
        if os.path.exists(self.download_path):
            os.remove(self.download_path)
            print(f"Removed {self.download_path}")

    def download_and_extract(self):
        if self.download_artifacts():
            self.extract_artifacts()
            self.cleanup()
