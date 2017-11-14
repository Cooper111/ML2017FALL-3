import keras
from keras.models import load_model
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.callbacks import ModelCheckpoint
import numpy as np
import csv
import os
import sys

output_path = './out.csv'

def load_data(test_data_path):
    X_test = []

    text = open(test_data_path, 'r', encoding='big5') 
    row = csv.reader(text , delimiter=",")
    for i,r in enumerate(row):
        if i == 0:
            continue
        X_test.append(r[1].split())



    return np.reshape(np.array(X_test),(len(X_test),48,48,1))


if __name__ == '__main__':
    test_data_path = 'data/test.csv'
    X_test = load_data(test_data_path)


    model = load_model('check_point/'+sys.argv[1])
    result = model.predict(X_test)
    y_ = np.argmax(result, axis=1)
    print('=====Write output to %s =====' % output_path)
    with open(output_path, 'w') as f:
        f.write('id,label\n')
        for i, v in  enumerate(y_):
            f.write('%d,%d\n' %(i, v))

