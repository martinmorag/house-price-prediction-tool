from sklearn.metrics import (
    mean_absolute_error,
    root_mean_squared_error,
    r2_score
)


def evaluate_model(y_true, predictions):
    """
    Compute regression metrics.

    Returns
    -------
    dict
        Dictionary containing MAE,
        RMSE and R².
    """

    return {
        "MAE": mean_absolute_error(
            y_true,
            predictions
        ),
        "RMSE": root_mean_squared_error(
            y_true,
            predictions
        ),
        "R2": r2_score(
            y_true,
            predictions
        )
    }