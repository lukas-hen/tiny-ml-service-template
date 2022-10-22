from os import listdir
from os.path import isfile, join
import pickle


def load_model(model_path: str):
    """
    Loads a model.
    """
    with open(model_path, "rb") as f:
        return pickle.loads(f.read())


def get_latest_model(models_path: str) -> str:
    """
    Fetches the latest model based on semver naming.
    """
    models = [
        f.strip(".pkl") for f in listdir(models_path) if isfile(join(models_path, f))
    ]
    models.remove("README.md")
    models.sort(key=lambda x: [int(y) for y in x.split(".")])
    models.reverse()
    return models[0]


def has_method(member_name: str, obj) -> bool:
    """
    Evaluates if method exists in object.
    """
    methods = [func for func in dir(obj) if callable(getattr(obj, func))]
    for method in methods:
        if method == member_name:
            return True
    return False
