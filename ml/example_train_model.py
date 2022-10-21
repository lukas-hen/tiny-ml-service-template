from sklearn.datasets import load_iris
from sklearn import tree
import pickle
import os
from dotenv import load_dotenv

load_dotenv(".env")

"""
Super simple model training example to generate small iris dataset ml models.
"""

model_version = os.getenv("MODEL_VERSION")

iris = load_iris()
X, y = iris.data, iris.target
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, y)

with open(f"ml_models/{model_version}.pkl", "wb") as f:
    pickle.dump(clf, f)
