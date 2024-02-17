import numpy as np


def detect_outliers_iqr(data):
        q1 = np.percentile(data, 25)
        q3 = np.percentile(data, 75)
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        low_outliers = [x for x in data if x < lower_bound]
        high_outliers = [x for x in data if x > upper_bound]
        return low_outliers, high_outliers