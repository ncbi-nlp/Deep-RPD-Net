"""
Detects RPD in dataset.

Usage:
    python .\classify_data.py "model_folder" "data_folder" "output_file"
"""


import sys 

import os

import numpy as np

import pandas as pd

import preprocessing

import trained_model

import tensorflow as tf


def classify_main(model_folder='./Models/AREDS2/Deep-RPD-Net+', data_folder='./Data/AREDS2', output='predictions.csv'):

            
    print('Loading Deep-RPD-Net')

    model = trained_model.load(model_folder)

    dataset = 'areds' if 'areds' in data_folder.lower() else 'daamd'


    if dataset == 'areds':
        
        scan_list = [d for d in os.listdir(data_folder) if os.path.isdir(os.path.join(data_folder, d))]
    
    else:

        scan_list = [file for file in os.listdir(data_folder) if file.endswith('.npy')]
    

    print('#scans in folder is', len(scan_list))
    
    predictions = []
    
    for scan_name in scan_list:
        
        print('predicting scan', scan_name.replace('.npy', ''))
        
        scan_path = os.path.join(data_folder, scan_name)
        
        scan = preprocessing.preprocess_scan(scan_path=scan_path, dataset=dataset)       
        
        scan = preprocessing.match_dims(scan)    
        
        pred = model.predict(scan, verbose=0)
        
        pred = np.argmax(pred[0])

        print(f'prediction is {pred}')

        predictions.append(pred)
    
    
    predictions = np.array(predictions)
    
    df = pd.DataFrame(predictions, columns=['prediction'])
    
    df.to_csv(output, index=False)
    
            

if __name__ == "__main__":

    print('Running ...')
        
    argv =  sys.argv[1:]

    # print(len(argv))

    # print(argv)
    
    

    if len(argv) == 3: # parameters are passed
    
        print('Taking args ...')

        model_folder = argv[0]

        data_folder = argv[1]

        output_file = argv[2]

        classify_main(model_folder, data_folder, output_file)
    
    else: # no parameters, using the defaults
        
        classify_main()
    





















