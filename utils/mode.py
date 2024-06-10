from typing import List
import numpy as np

def calculate_mode(series: List[float]) -> float:
    """
    Calculate the mode of a series of numbers.

    Parameters:
    series (List[float]): A list of numbers.

    Returns:
    float: The mode of the series.

    """
    counts, bins = np.histogram(series, bins=60)
    max_count_index = counts.argmax()
    mode = (bins[max_count_index] + bins[max_count_index + 1]) / 2
    return mode