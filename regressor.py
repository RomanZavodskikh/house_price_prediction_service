import joblib
import numpy as np
EPS = 1e-3

class Regressor(object):
    def __init__(self):
        self.model = joblib.load("hatas_model_dump.pkl")
    
    def predict_price(self, in_vector):
        try:
            predicted_price = self.model.predict(in_vector)[0]
            predicted_price = np.power(predicted_price, 2) - EPS
            predicted_price = round(predicted_price, 2)
            return predicted_price
        except:
            print("prediction error")
            return None 
