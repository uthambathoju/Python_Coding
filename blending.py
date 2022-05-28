import glob
import pandas as pd
import numpy as np

from sklearn import metrics

import config
if __name__ == "__main__":
    files = glob.glob(config.WRK_DIR+'model_preds/*.csv')
    df = None
    for f in files:
        if df is None:
            df = pd.read_csv(f)
        else:
            temp_df = pd.read_csv(f)
            df = df.merge(temp_df, on="id",how="left")

    print(df.head(10))

    targets = df.sentiment_x.values
    pred_cols = ["lr_pred", "lr_cnt_pred"]

    for col in pred_cols:
        auc = metrics.roc_auc_score(df.sentiment_x.values, df[col].values)
        print(f"{col}, auc={auc}")

    print("average")
    avg_pred = np.mean(df[["lr_pred", "lr_cnt_pred"]].values, axis=1)
    print(metrics.roc_auc_score(targets, avg_pred))


    print("weeighted-average")
    """ need optimization to arrive weights at gud number"""
    lr_pred = df.lr_pred.values
    lr_cnt_pred = df.lr_cnt_pred.values

    avg_pred =  (2 * lr_pred + lr_cnt_pred) / 4
    print(metrics.roc_auc_score(targets, avg_pred))

    avg_pred =  (3 * lr_pred + lr_cnt_pred) / 5
    print(metrics.roc_auc_score(targets, avg_pred)) 



    print("rank-averaging")
    lr_pred = df.lr_pred.rank().values
    lr_cnt_pred = df.lr_cnt_pred.rank().values

    avg_pred =  ( lr_pred + lr_cnt_pred) / 5
    print(metrics.roc_auc_score(targets, avg_pred)) 


    print("weighted rank-averaging")
    lr_pred = df.lr_pred.rank().values
    lr_cnt_pred = df.lr_cnt_pred.rank().values

    avg_pred =  (2 * lr_pred + lr_cnt_pred) / 4
    print(metrics.roc_auc_score(targets, avg_pred))

    avg_pred =  (3 * lr_pred + lr_cnt_pred) / 5
    print(metrics.roc_auc_score(targets, avg_pred)) 

