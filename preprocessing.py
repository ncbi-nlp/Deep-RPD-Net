import numpy as np

import skimage


import cv2

import matplotlib.pyplot as plt

import os

def normalize_scan(scan):

    scan = (scan - scan.min()) / (scan.max() - scan.min())

    scan = 2.0 * scan - 1.0
    
    return scan


def preprocess_scan(scan_path='.', dataset='areds'):

    if dataset=='areds':

        scan = preprocess_scan_areds(scan_path)
    
    else:

        scan = preprocess_scan_daamd(scan_path)

    
    return scan


def preprocess_scan_areds(scan_path):
            
    img_names = [img for img in os.listdir(scan_path) if img.endswith('.png')]
                        
    scan = []
            
    for img_name in img_names[2:-2]:

        img_path = os.path.join(scan_path, img_name)

        img = cv2.imread(img_path)

        if len(img.shape) > 2:

            img = img[:,:,0]

        if (img.shape[0] != 224) or (img.shape[1] != 448): 
            
            img = cv2.resize(img, (448, 224), cv2.INTER_CUBIC)   


        scan.append(img)

    scan = np.stack(scan, axis=-1) 
    
    scan = normalize_scan(scan)

    
    return scan


def preprocess_scan_daamd(scan_path):

    
    img_names = [img for img in os.listdir(scan_path) if img.endswith('.png')]
                        
    scan = []
            
    for img_name in img_names:

        img_path = os.path.join(scan_path, img_name)

        img = cv2.imread(img_path)

        if len(img.shape) > 2:

            img = img[:,:,0]

        if (img.shape[0] != 224) or (img.shape[1] != 448): 
            
            img = cv2.resize(img, (448, 224), cv2.INTER_CUBIC)   


        scan.append(img)

    scan = np.stack(scan, axis=-1) 
        
    scan = np.pad(scan, ((0, 0), (0, 0), (3, 4)), 'constant', constant_values=0)
                    
    output_shape =  (224, 448, 128)        
    
    scan = normalize_scan(scan)

    
    return scan



def match_dims(scan):
        
    scan = np.expand_dims(scan, axis=0)

    scan = np.expand_dims(scan, axis=-1)

    return scan
