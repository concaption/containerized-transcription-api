# containerized-transcription-api


```mermaid
graph LR
    setup[setup] -- "chmod +x ./setup.sh && ./setup.sh" --> install[install]
    install -- "pip install --upgrade pip && pip install -r requirements.txt" --> format[format]
    format -- "black ." --> lint[lint]
    lint -- 'find src -type f -name "*.py" -print0 | xargs -0 pylint' --> precommit[precommit]
    precommit -- "pre-commit install & pre-commit run --all-files" --> refactor[refactor]
    refactor -- "format precommit lint" --> push[push]
    push["push"] -- 'git add . && git commit -m $(m) && git push' --> docker[docker]
    docker -- "docker-compose up -d --build" --> run[run]
    run -- "python src/main.py" --> end[End]
```
