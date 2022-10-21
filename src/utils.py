from os import listdir
from os.path import isfile, join


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