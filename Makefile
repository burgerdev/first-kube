
REPO=docker.io/burgerdev

all: server client

server:
	docker build -t $(REPO)/palindrome:latest service
	docker push $(REPO)/palindrome:latest
	kubectl create -f service/palindromegen-pod.yaml
	kubectl create -f service/palindromegen-service.yaml

client:
	docker build -t $(REPO)/palindrome-client:latest pod
	docker push $(REPO)/palindrome-client:latest
	kubectl create -f pod/client-pod.yaml

.PHONY: all server client
