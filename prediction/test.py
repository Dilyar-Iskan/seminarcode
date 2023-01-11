import config
from feature_generator import FeatureGenerator

import keras
import pickle
from datetime import datetime
from model import net
import os 
accuracy_values = list()
accuracy_sum = 0.0
accuracy_value = 0.0
precision_values = list()
precision_sum = 0.0
precision_value = 0.0
recall_values = list()
recall_sum = 0.0
recall_value = 0.0
f1_values = list()
f1_sum = 0.0
f1_value = 0.0
training_time_seconds = list()

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
    args = config.load()
    
    if args.task == 'next_activity':
        loss = 'categorical_crossentropy'
        regression = False
    elif args.task == 'next_timestamp':
        loss = 'mae'
        regression = True

    # test the model*(real)
    checkpoint_dir = './checkpoints/'
    #modelname_next_act = 'modi_BPI_2012_dropna_filter_act.csv' + 'next_activity'
    modelname_next_time = 'modi_BPI_2012_dropna_filter_act.csv' + 'next_timestamp'

    # load prediction model
    #model_next_act = load_model(checkpoint_dir, modelname_next_act)
    model_next_time = load_model(checkpoint_dir, modelname_next_time)
    contextual_info = args.contextual_info


    # (CHANGED)
    est_dir = './estimation/'
    estname_next_time = 'modi_BPI_2012_dropna_filter_act.csv' + 'next_timestamp'
    # load estimation model
    est_next_time = load_model(est_dir, estname_next_time)

    # load the data 

    project_root = os.path.abspath(os.path.join(os.getcwd(), '..'))
    
    filename = os.path.join(project_root, args.data_dir, args.data_set ) 
    model_name = args.data_set + args.task

    # load data
    FG = FeatureGenerator()
    df = FG.create_initial_log(filename)

    test_df = df
    test_df = FG.order_csv_time(test_df)
    test_df = FG.queue_level(test_df)
    #test_df.to_csv('./test_data2.csv')
    state_list = FG.get_states(test_df)
    test_X, test_Y_Event, test_Y_Time = FG.one_hot_encode_history(test_df, args.checkpoint_dir+args.data_set)
    print('test_X shape:', test_X.shape)
    print('test_Y_Time shape:', test_Y_Time.shape)
    print('test_Y_Event shape:', test_Y_Event.shape)

    if contextual_info:
        test_context_X = FG.generate_context_feature(test_df,state_list)
        print('train_context_X shape:', test_context_X.shape)
        model = net()
        if regression:
            	
            scores = model_next_time.evaluate(test_X, test_context_X, test_Y_Time, loss)
            print('Test loss:', scores)