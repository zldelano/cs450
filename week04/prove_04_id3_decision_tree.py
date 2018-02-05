"""Implement ID3 algorithm to make a decision tree"""

import argparse
import pandas as pd
import numpy as np
from anytree import Node, RenderTree
from collections import Counter

COLS_CLASS_EXAMPLE = ["Credit Score", "Income", "Collateral", "Should Loan"]
COLS_CLASS_EXAMPLE_TRAIN = ["Credit Score", "Income", "Collateral"]

class MyDecisionTreeClassifier:
    """my class for the Decision Tree"""
    def __init__(self):
        pass
    
    def fit(self, train_data, train_target):
        """fit the data"""
        return DTCModel(train_data, train_target)

class DTCModel:
    _train_data = None
    _train_target = None
    _tree = None

    def __init__(self, train_data, train_target):
        """put the data in the model"""
        self._train_data = train_data
        self._train_target = train_target
        classes = []
        self._make_ID3_tree([0], self._train_data, self._train_target)

    def _calc_entropy(self, numers, denom):
        """calc the entropy for this particular attribute's value"""
        total_entropy = 0
        for numer in numers:
            p = numer / float(denom)
            total_entropy -= (p * np.log2(p))
        return total_entropy

    def _calc_entropies_aux(self, array_dicts):
        """calculate the entropy of each attribute, helper function"""
        entropies = []
        for i_dict in array_dicts:
            numers = []
            weight = 0
            sum_weight = 0
            sum_entropy = 0
            for key in i_dict:
                # this will be needed to compute the average entropy between values of attributes
                weight = len(i_dict[key])
                for key, value in Counter(i_dict[key]).iteritems():
                    numers.append(value)
                # make a sum of total entropy
                sum_entropy += self._calc_entropy(numers, weight) * weight
                sum_weight += weight
                numers = []
            entropy = sum_entropy / float(sum_weight)
            # make a list of our entropies
            entropies.append(entropy)

        return entropies

    def _calc_entropies(self, train_data, train_target):
        """calculate the entropy of each attribute"""
        buckets = []
        feats = []
        cidx = 0
        for feat in train_data.columns:
            # store the column index in along with the column name
            buckets.append({})
            feats.append(feat)
            for ridx, row in train_data[feat].iteritems():
                if row in buckets[cidx]:
                    buckets[cidx][row].append(train_target[ridx])
                else:
                    buckets[cidx][row] = []
                    buckets[cidx][row].append(train_target[ridx])
            cidx += 1
        # turn this into a dictionary of column names with their values as the entropies
        entropies_dict = {}
        entropies = self._calc_entropies_aux(buckets)
        e_count = 0
        for entropy in entropies:
            entropies_dict[feats[e_count]] = entropy
            e_count += 1
        return entropies_dict

    def _make_ID3_tree(self, classes, train_data, train_target):
        """make the ID3 decision tree"""
        print self._calc_entropies(train_data, train_target)
        if train_data.empty or len(train_data.columns) == 0:
            # reached an empty branch
            None
        elif classes.count(classes[0]) == train_data.size / len(train_data.columns):
            return classes[0]

    def predict(self, test_data):
        """"""
        pass

def receive_args():
    """pass arguments to the script"""
    parser = argparse.ArgumentParser(description='Pass arguments to the script')
    parser.add_argument('--csv_file',
                        dest='csv_file',
                        action='store',
                        choices=["id3_class.csv", "iris.csv"],
                        required=True)

    return parser

def load_csv_file_class_example(args):
    """open csv file"""
    cols = COLS_CLASS_EXAMPLE
    df = pd.io.parsers.read_csv(
        args.csv_file,
        header=None,
        usecols=list(range(len(cols))),
        names=cols,
        delim_whitespace=True
    )
    return df

def prep_data_class_example(df):
    """prepare the data for the class example set"""
    df["Credit Score"] = df["Credit Score"].astype('category').cat.codes
    df["Income"] = df["Income"].astype('category').cat.codes
    df["Collateral"] = df["Collateral"].astype('category').cat.codes
    df["Should Loan"] = df["Should Loan"].astype('category').cat.codes
    df_target = df['Should Loan']
    df.drop(columns=['Should Loan'], inplace=True)

    return df, df_target

def prep_data(args):
    """prepare the data from one of the datasets"""
    train_data = None
    test_data = None
    train_target = None
    test_target = None
    if args.csv_file == "id3_class.csv":
        train_data, train_target = prep_data_class_example(load_csv_file_class_example(args))
    else:
        raise ValueError("the script is not ready for this filename")

    return train_data, test_data, train_target, test_target

def main():
    """everything happens here"""
    args = receive_args().parse_args()
    train_data, test_data, train_target, test_target = prep_data(args)
    model = MyDecisionTreeClassifier().fit(train_data, train_target)

main()