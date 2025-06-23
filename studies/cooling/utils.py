import numpy as np

def running_average(x, y, bins):
     """
     Compute the running average of y over fixed intervals in x efficiently using NumPy.

    Parameters:
    x (array-like): Array of x-values (sorted or unsorted).
    y (array-like): Array of y-values corresponding to x.
    interval_width (float): The width of the intervals.

    Returns:
    bin_centers (numpy.ndarray): The centers of the bins.
    averages (numpy.ndarray): The average y-values for each bin.
     """
    # Ensure inputs are NumPy arrays
     x = np.array(x)
     y = np.array(y)

    # Bin the data using NumPy digitize
     bin_indices = np.digitize(x, bins) - 1  # Get zero-based bin indices

    # keep only elements within bins
     valid_input_indices = (bin_indices > 0) & (bin_indices < len(bins) - 1)

    # Preallocate array for averages
     averages = np.zeros(len(bins) - 1, dtype=float)
    
    # Use NumPy's bincount for fast bin-based summation and counts
     bin_sums   = np.bincount(bin_indices[valid_input_indices], minlength=len(bins) - 1, weights=y[valid_input_indices])
     bin_counts = np.bincount(bin_indices[valid_input_indices], minlength=len(bins) - 1)
    
    # Avoid division by zero: compute averages where bin_counts > 0
     non_empty_bins = bin_counts > 0
     averages[non_empty_bins] = bin_sums[non_empty_bins] / bin_counts[non_empty_bins]

    # Compute bin centers
     bin_centers = (bins[:-1] + bins[1:]) / 2

     return bin_centers, averages, bin_counts, bin_sums


