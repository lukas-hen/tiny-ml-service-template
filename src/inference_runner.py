from models.inference import InferenceInput, InferenceResponse
import numpy as np
from datetime import datetime


def infer(data: list[InferenceInput], model) -> list[InferenceResponse]:
    """
    Inference function.

    Model specific implementation that takes API DAO and returns parsed response.
    """
    results = []
    for item in data:
        inference_result = model.predict(
            np.array(
                [
                    [
                        item.sepal_length,
                        item.sepal_width,
                        item.petal_length,
                        item.petal_width,
                    ]
                ]
            )
        )

        results.append(
            InferenceResponse(
                input=item,
                inference_result=inference_result,
                inference_ts=datetime.now().isoformat(),
            )
        )

    return results
