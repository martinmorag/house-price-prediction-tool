from pathlib import Path

# Project root directory
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Paths
DATA_PATH = PROJECT_ROOT / "data" / "raw" / "houses.csv"
MODEL_PATH = PROJECT_ROOT / "models" / "best_model.pkl"

# Target column
TARGET_COLUMN = "Price"

# Feature lists
NUMERICAL_FEATURES = [
    "Area_SqFt",
    "Rooms",
    "Build_Year"
]

CATEGORICAL_FEATURES = [
    "Location",
    "Street_Type",
    "Furnishing",
    "Property_Type",
    "Has_Pool"
]