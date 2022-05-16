import os
import pandas as pd
from sklearn import model_selection 


if __name__ == "__main__":
    df = pd.read_csv(os.environ.get("WRK_DIR"))
    df['kfold'] = -1
    df = df.sample(frac=1).reset_index(drop=True)
    y = df['LICENSE STATUS'].values

    #initiate kfold
    kf = model_selection.StratifiedKFold(n_splits=5)
    #fill the new kfold
    for fold, (train_idx, val_idx) in enumerate(kf.split(X=df, y=y)):
        df.loc[val_idx, 'kfold'] = fold

    df.to_csv(os.environ.get("WRK_DIR") + "/train_folds.csv", index=False)
