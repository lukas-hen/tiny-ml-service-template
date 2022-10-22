# Tiny ML service template
Template for a small ML model deployment. Pickled ml models are stored in the ml folder named as semver tags. For an example, see `example_train_model.py`

## Building and running container
For simple building & running you can use the provided makefile.
To build your container, run `make build`
To run the latest container, run `make run`

## Linting
For linting black is used. If you don't already have it installed locally, please run `make deps`.
Then you can lint your code by running `make lint`

## Docs
When you launch the container, FastApi gives you api docs out of the box. Please run the container and see localhost:8000/docs

## TODO
* ~Add support for multiline inference.~
* Add proper exception handling
* Add better logging
* Add scoring functionality & endpoint to get model score.
* Separate out dev deps from prod image.