import os
import joblib

BASE_DIR = os.path.dirname(__file__)

model_files = {
    'linear': 'linear.pkl',
    'ridge': 'ridge.pkl',
    'lasso': 'lasso.pkl',
    'random_forest': 'random_forest.pkl'
}

models = {
    name: joblib.load(os.path.join(BASE_DIR, file))
    for name, file in model_files.items()
}
