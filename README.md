# devops-qa-project
## Description
Project related to devops activities - creating simple server, preparing IaC file with Ansible, creating Dockerfile and Makefile and creating Jenkins file with Groovy for dedicated pipeline

## Prerequisites
1. Install python >=3.13.
2. Install pipx. Docs: https://pipx.pypa.io/stable/installation/
3. Install uv project manager. Docs: https://docs.ansible.com/projects/ansible/latest/installation_guide/intro_installation.html
4. Install ansible. Docs: https://docs.ansible.com/projects/ansible/latest/installation_guide/intro_installation.html
5. Install Docker (Desktop). Docs: https://docs.docker.com/desktop/

## Run
1. Run fastapi server directly:
`uv run fastapi dev`

2. Run fastapi server with ansible:
`ansible-playbook -i inventory.ini deploy_fastapi.yml --ask-become-pass`

3. Run fastapi server with Docker:
* Build image:
```docker build -t task-runner .```
* Mode: hello
```docker run --rm task-runner hello --api-url http://<IP_address>:8000 --output-file hello.txt```
* Mode: random
```docker run --rm task-runner random --api-url http://<IP_address:8000 --hostname <remote_IP> --username <username> --password <password> --remote-filename random_phrase```

4. Run with Make:
```make build```