IMG_TAG=ml-service-img

build:
	docker build -t $(IMG_TAG) .

run:
	docker run -p 8000:8000 $(IMG_TAG)

example: # Train example model. Requires model version semver to be set in .env.
	python ml/example_train_model.py

lint:
	black .

deps:
	pip install -r requirements.txt