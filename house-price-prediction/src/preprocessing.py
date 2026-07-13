from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

from sklearn.preprocessing import (
    StandardScaler,
    OneHotEncoder
)

from sklearn.impute import SimpleImputer

from .config import (
    NUMERICAL_FEATURES,
    CATEGORICAL_FEATURES
)


def create_preprocessor():
    """
    Create the preprocessing pipeline used
    throughout the project.
    """

    numeric_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler())
    ])

    categorical_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        (
            "encoder",
            OneHotEncoder(handle_unknown="ignore")
        )
    ])

    return ColumnTransformer([
        (
            "num",
            numeric_pipeline,
            NUMERICAL_FEATURES
        ),
        (
            "cat",
            categorical_pipeline,
            CATEGORICAL_FEATURES
        )
    ])