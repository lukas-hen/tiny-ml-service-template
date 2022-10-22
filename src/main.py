from fastapi import FastAPI
from models.inference import InferenceInput, InferenceResponse
from inference_runner import infer
from utils import has_method
from os import listdir
from os.path import isfile, join
import logging
import pickle

models_path = "ml_models"

app = FastAPI()


@app.on_event("startup")
async def startup():

    """
    Initial check that all given models implement the predict method.
    """

    model_paths = [
        join(models_path, f)
        for f in listdir(models_path)
        if isfile(join(models_path, f)) and ".pkl" in f
    ]

    model_files = [open(path, "rb") for path in model_paths]

    deserialized_models = [pickle.loads(model.read()) for model in model_files]

    for model in zip(model_paths, deserialized_models):
        if not has_method("predict", model[1]):
            logging.error(
                f"The predict method is not implemented for model at: {model[0]}"
            )

    """ Close models """
    for model_file in model_files:
        model_file.close()


@app.post("/api/infer")
async def predict_latest_model(data: InferenceInput):
    """
    Run inference using the latest model SemVer.

    Api endpoint to run inference, but automatically choose the latest model.
    """
    model_version = get_latest_model(models_path)
    return infer(data, model_version)


@app.post("/api/infer/{model_version}")
async def predict_specific_model(data: InferenceInput, model_version: str):
    """
    Run inference using specific model version.

    Api endpoint to run inference using the provided model version in the url path.
    """
    return infer(data, model_version)
