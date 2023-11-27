#
# test_container Makefile: build and push a container to run test_fucntion
#

REPO=damonreed
IMAGE=test_container
TAG=latest

build: Dockerfile
	docker build -t $(REPO)/$(IMAGE):$(TAG) .

run:
	docker run --rm -d -p 8080:8080 -e PORT=8080 --name test_container $(REPO)/$(IMAGE):$(TAG)
	sleep 2
	curl http://localhost:8080
	sleep 2
	docker stop test_container

push: 
	docker push $(REPO)/$(IMAGE):$(TAG)

requirements: requirements.txt
	pip install --no-cache-dir -r ./requirements.txt

local-test:
	functions-framework --target=test --debug 


