from models.inference import InferenceInput, InferenceResponse
import pickle
import numpy as np
from datetime import datetime


def infer(data: InferenceInput, model_version: str) -> InferenceResponse:
    """
    Inference "drivers"

    Example implementation of model inference. Has to be altered depending on the model.
    """
    with open(f"ml_models/{model_version}.pkl", "rb") as f:
        clf = pickle.loads(f.read())

    inference_result = clf.predict(
        np.array(
            [[data.sepal_length, data.sepal_width, data.petal_length, data.petal_width]]
        )
    )
    return InferenceResponse(
        **{
            "inference_result": inference_result[0],
            "model_version": model_version,
            "inference_ts": datetime.now().isoformat(),
        }
    )
