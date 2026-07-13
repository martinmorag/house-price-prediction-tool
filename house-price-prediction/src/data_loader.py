import pandas as pd
from .config import DATA_PATH


def load_data():
    """
    Load the house price dataset.

    Returns:
        pandas.DataFrame: Raw dataset.
    """
    return pd.read_csv(DATA_PATH)