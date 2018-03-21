import sklearn
import numpy as np
import pandas as pd

COLS_CHESS  = ["wk_file", "wk_rank", "wr_file", "wr_rank", "bk_file", "bk_rank", "depth_of_win"]
COLS_IRIS   = ["sepal_len", "sepal_wid", "petal_len", "petal_wid", "class"]
COLS_LETTER = ["letter", "x-box", "y-box", "wid-wid", "high-height", "onpix", "x-bar", "y-bar",
               "x2bar", "y2bar", "xybar", "x2ybr", "xy2br", "x-ege", "xegvy", "y-ege", "yegvx"]

def read_csv(cols, filename):
    return pd.io.parsers.read_csv(
        filename,
        header=None,
        usecols=list(range(len(cols))),
        names=cols
    )

def get_chess_dataset_categorical():
    df = read_csv(COLS_CHESS, "week11\\chess.csv")

    return df

def get_letter_dataset_categorical():
    df = read_csv(COLS_LETTER, "week11\\letter.csv")

    return df

def get_iris_dataset_categorical():
    df = read_csv(COLS_IRIS, "week11\\iris.csv")

    return df

def get_chess_dataset_numerical():
    df = read_csv(COLS_CHESS, "week11\\chess.csv")

    return df

def get_letter_dataset_numerical():
    df = read_csv(COLS_LETTER, "week11\\letter.csv")

    return df

def get_iris_dataset_numerical():
    df = read_csv(COLS_IRIS, "week11\\iris.csv")

    return df

def main():
    """magic happens here"""
    # preprocessing
    df_iris_num = get_iris_dataset_numerical()
    df_iris_cat = get_iris_dataset_categorical()
    # For each dataset

    ## Try at least 3 different "regular" learning algorithms and note the results.
    ### DS1
    ##### method 1
    ##### method 2
    ##### method 3
    ### DS2
    ##### method 1
    ##### method 2
    ##### method 3
    ### DS3
    ##### method 1
    ##### method 2
    ##### method 3

    ## Use Bagging and note the results. (Play around with a few different options)
    ### DS1
    ### DS2
    ### DS3

    ## Use AdaBoost and note the results. (Play around with a few different options)
    ### DS1
    ### DS2
    ### DS3

    ## Use a random forest and note the results. (Play around with a few different options)
    ### DS1
    ### DS2
    ### DS3

main()