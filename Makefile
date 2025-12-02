IMAGE_NAME=task-runner
DOCKERFILE=Dockerfile

.PHONY: build

build:
	docker build -t $(IMAGE_NAME) -f $(DOCKERFILE) .