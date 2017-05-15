
all: server client

server:
	docker build -t palindrome:latest server
	kubectl create -f server/palindromegen-pod.yaml
	kubectl create -f server/palindromegen-service.yaml

client:
	docker build -t palindrome-client:latest
	kubectl create -f pod/client-pod.yaml

.PHONY: all server client
