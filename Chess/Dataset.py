import pandas as pd
import os
import csv

class Dataset:

    data = []

    def write():
        pd.DataFrame(Dataset.data).drop_duplicates().to_csv("./Chess/dataset.csv", index=False, header=None)

    def read():
        if os.path.exists("./Chess/dataset.csv"):
            with open('./Chess/dataset.csv', newline='') as file:
                reader = csv.reader(file)
                Dataset.data = list(reader)
                print("Dataset entries: " + str(len(Dataset.data)))
