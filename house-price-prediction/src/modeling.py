from sklearn.pipeline import Pipeline


def build_pipeline(preprocessor, model):
    """
    Combine preprocessing and model
    into a single Scikit-Learn pipeline.
    """

    return Pipeline([
        ("preprocessor", preprocessor),
        ("model", model)
    ])