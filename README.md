# Code Checkers Parser

## Supported checkers:
- **Radon CC & MI** (Tested on versions: ```6.0.1```)
- **Ruff** (Tested on versions: ```0.1.8```)
- **Bandit** (Tested on versions: ```1.7.6```)


## How to use
### 1. Clone repository
```commandline
git clone https://github.com/vsaverin/checkers_parser
```

### 2. Setup project
#### 2.1 Create .env file in project root
Example:
```
SECRET_KEY = "string"
GITLAB_URL = "https://url.com"
PROJECT_ID = "id"
JOB_NAME = "your_job_name"
ACCESS_TOKEN = "access_token"
POSTGRES_DB = "local_db"
POSTGRES_USER = "local_user"
POSTGRES_PASSWORD = "qwerty123321"
```
#### 2.2 In **settings.py** specify your reports filenames:
```python
BANDIT_FILENAME = 'bandit.txt'
RUFF_FILENAME = 'ruff.json'
RADON_MI_FILENAME = 'radon_mi.txt'
RADON_CC_FILENAME = 'radon_cc.txt'
```
Also don't forger to replace default **ALLOWED_HOSTS** with yours
```python
ALLOWED_HOSTS = [
    "your_address:8008"
]
```

### 3. Build!
```commandline
poetry lock --no-update
docker-compose -f deploy/docker-compose.yml up --build
```

#### After successful build service will be available on port 8008 by default

## Services requires Admin authentication! 
### Don't forget to create superuser:
```commandline
docker container exec -it container-name /bin/sh 
python3 manage.py createsuperuser
```

## ToDo:
- Refactoring
- Multiple projects support
- Errors catching (with ui)