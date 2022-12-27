 

import pandas as pd
import numpy as np
import tensorflow
from tensorflow.keras.models import load_model
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.preprocessing.sequence import TimeseriesGenerator

from tensorflow.keras.models import load_model
model = load_model('btc_model_1.h5')
result = None

def process(test):
    global result
    data1 = test
    data2 = data1[:5]
    
    data_y_scaler = data2.drop(columns=['<OPEN>', '<HIGH>', '<LOW>', '<VOL>'])
    x_data = data2.to_numpy()
    
    x_scaler = StandardScaler()
    x_scaler.fit(x_data)
    x_data_train = x_scaler.transform(x_data)
    
    y_scaler = StandardScaler()
    y_scaler.fit(data_y_scaler)
    y_data_train = y_scaler.transform(data_y_scaler)
    
    generator = TimeseriesGenerator(x_data_train, x_data_train, length=4, batch_size=1)

    
    x_predict, y_test = generator[0]
    model_predict = y_scaler.inverse_transform(model.predict(x_predict))

    
    pred_list = list(model_predict)
    pred_list = pred_list[0]
    result = ''.join(map(str, pred_list))
    return result



