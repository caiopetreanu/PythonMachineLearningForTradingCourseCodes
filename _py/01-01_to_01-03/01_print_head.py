import pandas as pd

def run_rest():
    """Function called by Test Run."""
    df = pd.read_csv("C:/study/video/udacity/Machine_Learning_for_Trading/_data/APPL.csv")
    print(df.head())


if __name__ == "__main__":
    run_rest()