import numpy as np
from scipy.stats import ks_2samp


def detect_drift(reference_df, current_df, threshold=0.05):
    """
    Detect data drift using Kolmogorov–Smirnov test.
    Returns True if drift is detected.
    """

    drifted_features = 0
    total_features = reference_df.shape[1]

    for col in reference_df.columns:
        stat, p_value = ks_2samp(reference_df[col], current_df[col])

        if p_value < threshold:
            drifted_features += 1

    drift_ratio = drifted_features / total_features

    # Drift if >30% features drifted
    return drift_ratio > 0.3
