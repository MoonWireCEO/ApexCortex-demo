
from sklearn.linear_model import LogisticRegression
import numpy as np

def train_logreg(X, y):
    clf = LogisticRegression(max_iter=500)
    clf.fit(X, y)
    return clf

def to_signal(proba, threshold: float = 0.5):
    return (proba >= threshold).astype(float) * 2 - 1
