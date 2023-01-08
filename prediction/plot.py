import config
from feature_generator import FeatureGenerator

import keras
import pickle
from datetime import datetime
from model import net
import os 


args = ""

def load_model(checkpoint_dir, model_name):
    """load prediction model

    Keyword arguments:
    checkpoint_dir -- directory path
    model_name -- decide which model to load
    """
    model = net()
    model.load(checkpoint_dir, model_name)
    return model
if __name__ == '__main__':
    checkpoint_dir = './prediction/checkpoints/'
    modelname_next_act = 'traininglog_0806_1.csv' + 'next_activity'
    modelname_next_time = 'traininglog_0806_1.csv' + 'next_timestamp'
    # load prediction model
    model_next_act = load_model(checkpoint_dir, modelname_next_act)
    model_next_time = load_model(checkpoint_dir, modelname_next_time)
    dir = './plots/test/'
    to_file= modelname_next_act + '.png'
    model_next_act.plot(dir=dir, to_file=to_file)
    to_file = modelname_next_time + '.png'
    model_next_time.plot(dir=dir, to_file=to_file)

    checkpoint_dir = './prediction/checkpoints/'
    modelname_next_act = 'modi_BPI_2012_dropna_filter_act.csv' + 'next_activity'
    modelname_next_time = 'modi_BPI_2012_dropna_filter_act.csv' + 'next_timestamp'
    # load prediction model
    model_next_act = load_model(checkpoint_dir, modelname_next_act)
    model_next_time = load_model(checkpoint_dir, modelname_next_time)
    dir = './plots/real/'
    to_file= modelname_next_act + '.png'
    model_next_act.plot(dir=dir, to_file=to_file)
    to_file = modelname_next_time + '.png'
    model_next_time.plot()

    # (CHANGED)
    est_dir = './prediction/estimation/'
    estname_next_time = 'modi_BPI_2012_dropna_filter_act.csv' + 'next_timestamp'
    # load estimation model
    est_next_time = load_model(est_dir, estname_next_time)
    to_file= estname_next_time + '.png'
    est_next_time.plot(dir=dir, to_file=to_file)