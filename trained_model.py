"""
Loading trained model
"""

import tensorflow as tf

from tensorflow.keras.models import *


import sys

import os


def load(model_path='./Models/AREDS2/Deep-RPD-Net+'):               
    
    model = load_model(model_path)
           
    return model