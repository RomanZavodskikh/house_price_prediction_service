import joblib

class Regressor(object):
    def __init__(self):
        self.model = joblib.load("hatas_model_dump.pkl")
    
    def predict_price(self, in_vector):
        try:
            return self.model.predict(in_vector)[0]
        except:
            print("prediction error")
            return None 
