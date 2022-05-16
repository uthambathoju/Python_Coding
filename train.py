import os
import joblib
import pandas as pd

from sklearn import metrics
from sklearn import linear_model
from sklearn import preprocessing

#models
import model_dispatcher as dispatcher
import config



def train(df, MODEL):
    """
    :param df: pandas dataframe with train/test data
    :return score: f1_score
    """
    for fold in range(5):
        #features
        df_train = df[df["kfold"] != fold].reset_index(drop=True)
        df_valid = df[df["kfold"] == fold].reset_index(drop=True)
        #target
        ytrain = df_train['LICENSE STATUS'].values
        yvalid = df_valid['LICENSE STATUS'].values

        drop_cols = ["ID","LICENSE STATUS","kfold"]
        df_train = df_train.drop(drop_cols, axis=1)
        df_valid = df_valid.drop(drop_cols, axis=1)
        #model
        clf = dispatcher.MODELS[MODEL]
        preds = clf.predict_proba(df_valid)[:, 1]
        score = metrics.f1_score(yvalid, preds)

        #save model , cols
        joblib.dump(clf, f'./models/{MODEL}_{fold}.pkl')
        joblib.dump(df_train.columns, f'./models/{MODEL}_{fold}_columns.pkl')

if __name__ == "__main__":
    MODEL = os.environ.get('MODEL')
    df = pd.read_csv(os.environ.get("TRAINING_FOLDS"))
    train(df, MODEL)