# containerized-transcription-api

[![Docker](https://github.com/buildberg/containerized-transcription-api/actions/workflows/docker-publish.yml/badge.svg)](https://github.com/buildberg/containerized-transcription-api/actions/workflows/docker-publish.yml)

![](screenshot.png)
### Overview
This project sets up a robust web application using FastAPI. It integrates the open-source Whisper AI model for Speech-to-Text (STT) transcription, enabling accurate and efficient audio-to-text conversion. The application is containerized using Docker, ensuring consistent and efficient runtime in any environment.
### Features
* **FastAPI Backend:** A high-performance, easy-to-learn backend.
* **Whisper AI Integration:** Cutting-edge STT transcription.
* **Dockerized:** Simplified deployment, scalability, and management.
### Why this project?
Whether you want to automate your transcription tasks, enhance accessibility for your content, or explore the world of AI-powered applications, this project has you covered.
### Installation
1. Clone the repository
```
git clone https://github.com/buildberg/containerized-transcription-api
```
2. Navigate into the project folder
```
cd containerized-transcription-api
```
3. Build and run Docker container
```
make docker
```

### Usage
Convert Audio to Text
```bash
POST /whisper
```
Body Params: **audio_file: file**

```mermaid
graph LR
  setup[make setup]
  setup -->|1. Make script executable| setup.sh[setup.sh]
  setup -->|2. Run script| setup.sh

  install[make install]
  install -->|1. Upgrade pip| pip[pip]
  install -->|2. Install requirements| requirements[requirements.txt]

  format[make format]
  format -->|Format all code| black[Black]

  lint[make lint]
  lint -->|Find and lint .py files| pylint[Pylint]

  precommit[make precommit]
  precommit -->|1. Install pre-commit hooks| pre-commit-install[pre-commit install]
  precommit -->|2. Run hooks on all files| pre-commit-run[pre-commit run]

  refactor[make refactor]
  refactor --> format
  refactor --> precommit
  refactor --> lint

  push[make push]
  push -->|1. Add changes| git-add[git add]
  push -->|2. Commit changes| git-commit[git commit]
  push -->|3. Push to repository| git-push[git push]

  docker[make docker]
  docker -->|1. Docker-compose build and up| docker-compose[docker-compose up -d --build]

  run[make run]
  run -->|1. Execute main script| main-script[python src/main.py]

```
