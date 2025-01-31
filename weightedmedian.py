import numpy as np
def weighted_median(parallax_values, parallax_errors):
    values = np.array(parallax_values)
    weights = 1/((np.array(parallax_errors))**2)
    sort_indices = np.argsort(values)
    sorted_values = values[sort_indices]
    sorted_weights = weights[sort_indices]
    cumsum = sorted_weights.cumsum()
    cutoff = sorted_weights.sum() / 2.
    return sorted_values[cumsum >= cutoff][0]