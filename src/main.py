from fastapi import FastAPI
from models.inference import InferenceInput
from inference_runner import infer
from startup_checks import assert_all_models_implement_predict
from utils import get_latest_model, load_model

models_path = "ml_models"

app = FastAPI()


@app.on_event("startup")
async def startup():
    assert_all_models_implement_predict(models_path)


@app.post("/api/infer")
async def predict_latest_model(data: list[InferenceInput]):
    """
    Run inference using the latest model SemVer.

    Api endpoint to run inference, but automatically choose the latest model.
    """
    model_version = get_latest_model(models_path)
    model = load_model(f"{models_path}/{model_version}.pkl")
    return infer(data, model)


@app.post("/api/infer/{model_version}")
async def predict_specific_model(data: list[InferenceInput], model_version: str):
    """
    Run inference using specific model version.

    Api endpoint to run inference using the provided model version in the url path.
    """
    model = load_model(f"{models_path}/{model_version}.pkl")
    return infer(data, model)
