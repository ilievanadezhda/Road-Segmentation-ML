"""Postprocessing functions."""

from skimage.morphology import (
    square,
    opening,
    erosion,
)


def apply_morphological_operations(prediction):
    """Applies morphological operations to the prediction.

    Args:
        prediction: predicted labels

    Returns:
        thinned_prediction: prediction after morphological operations
    """
    # opening to the combined image to remove small white spots
    cleaned_prediction = opening(prediction, square(3))
    # erosion to thin up the roads
    thinned_prediction = erosion(cleaned_prediction, square(9))
    return thinned_prediction
