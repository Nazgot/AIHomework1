import pandas as pd
import os
import csv

class Dataset:

    data = []

    def write():
        pd.DataFrame(Dataset.data).drop_duplicates().to_csv("./dataset.csv", index=False, header=None)

    def read():
        if os.path.exists("./dataset.csv"):
            with open('./datasets/heuristics.csv', newline='') as file:
                reader = csv.reader(file)
                Dataset.data = list(reader)
                print("Dataset entries: " + str(len(Dataset.data)))
