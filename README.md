# Code Checkers Parser

#### *last project stable version is on branch "Stable"

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

## !!! Services requires Superuser authentication !!! 
### 4. Create superuser:
```commandline
docker container exec -it container-name /bin/sh 
python3 manage.py createsuperuser
```

### 5. Connect your GitLab project using django admin:
#### 5.1 Goto:
```
https://yourhost.com/admin
```
#### 5.2 Open Application
```commandline
MAIN -> GitlabProjects
```
#### 5.3 Create New Object
```
- Project name: Your Custom project name (will be displayed on dashboard)
- Project Id: id of the gitlab project u want to connect
- Analysis job name: name of the analysis stage in ur pipeline
- Bandit filename: name of file to search in ur gitlab artifacts (ex. bandit.json)
- Ruff filename: name of file to search in ur gitlab artifacts (ex. ruff.json)
- Radon mi filename: name of file to search in ur gitlab artifacts (ex. radon_mi.json)
- Radon cc filename: name of file to search in ur gitlab artifacts (ex. radon_cc.json)
```


## ToDo:
- ~~Refactoring~~
- ~~Multiple projects support~~
- Projects artifacts auto-update (by last proceeded job id)
- Move Dashboard & Projects to different app
- Errors catching (with ui)