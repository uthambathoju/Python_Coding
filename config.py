import os
import sys 

os.environ['WRK_DIR'] = 'D:/Utham/ZS/data/'
os.environ['TRAINING_DATA'] = 'D:/Utham/ZS/data/input/train.csv'
os.environ['TRAINING_FOLDS'] = 'D:/Utham/ZS/data/input/train_folds.csv'
os.environ['TESTING_DATA'] = 'D:/Utham/ZS/data/input/test.csv'
os.environ['MODEL'] = sys.argv[1]
os.environ['FOLD'] = sys.argv[2]
