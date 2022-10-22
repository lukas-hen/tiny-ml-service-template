from pydantic import BaseModel

"""
Python DAO:s
"""


class InferenceInput(BaseModel):
    """
    Example input for the Iris dataset.
    """

    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


class InferenceResponse(BaseModel):
    """
    Example response for the Iris dataset.
    """

    input: InferenceInput
    inference_result: float
    inference_ts: str
