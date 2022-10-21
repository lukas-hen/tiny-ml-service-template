IMG_TAG=ml-service-img

build:
	docker build -t $(IMG_TAG) .

run:
	docker run $(IMG_TAG)