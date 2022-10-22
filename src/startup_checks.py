import pickle
import logging
from utils import has_method
from os import listdir
from os.path import isfile, join


def assert_all_models_implement_predict(models_path):
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
