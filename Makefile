IMG_TAG=ml-service-img

build:
	docker build -t $(IMG_TAG) .

run:
	docker run -p 8000:8000 $(IMG_TAG)