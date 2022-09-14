
import pandas as pd
def load_data():
    dataset = pd.read_csv("dimond.csv")
    return dataset

load_data()
