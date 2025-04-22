import pandas as pd
import numpy as np

def load_data(filename):
    df = pd.read_csv(filename, sep=",", index_col=False)
    df.columns = ["housesize", "rooms", "price"]
    data = np.array(df, dtype=float)
    # plot_data(data[:, :2], data[:, -1])
    # normalize(data)
    return data[:,:2], data[:, -1]

