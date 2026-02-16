from sklearn.ensemble import RandomForestRegressor
from .base import VolatilityModel

class RFVolModel(VolatilityModel):
    def __init__(self, **params):
        self.model = RandomForestRegressor(**params)

    def fit(self, X, y):
        self.model.fit(X, y)
        return self

    def predict(self, X):
        return self.model.predict(X)
