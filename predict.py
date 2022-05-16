import os
import joblib
import pandas as pd
import numpy as np

from sklearn import metrics


def predict(df, MODEL):
    test_idx = df["ID"].values
    predictions= None

    for fold in range(5):
        #load model and columns
        columns = joblib.load(os.path.join("./models/", f'{MODEL}_{fold}_columns.pkl'))
        clf = joblib.load(os.path.join("./models/", f'{MODEL}_{fold}.pkl'))
        df =df[columns]
        preds = clf.predict_proba(df)[:, 1]
        #append preds in each fold
        if fold == 0:
            predictions = preds
        else:
            predictions += preds

    #avg of all folds preds
    predictions /= 5
    sub = pd.DataFrame(np.columnstack((test_idx, predictions)), columns=['ID', 'LICENSE STATUS'])
    return sub



if __name__ == "__main__":
    TEST_DATA = os.environ.get("TEST_DATA")
    MODEL = os.environ.get("MODEL")
    df = pd.read_csv(TEST_DATA)
    sub = predict(df, MODEL)
    sub.to_csv(f'./models/{MODEL}.csv', index=False)