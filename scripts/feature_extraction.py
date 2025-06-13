import numpy as np

def extract_features(theta, alpha, beta):
    """
    Extracts basic statistical features from EEG signal bands.

    Parameters:
        theta (np.ndarray): Theta band signal (4–8 Hz)
        alpha (np.ndarray): Alpha band signal (8–12 Hz)
        beta  (np.ndarray): Beta band signal (12–30 Hz)

    Returns:
        dict: Dictionary of extracted features
    """
    features = {
        'theta_mean': np.mean(theta),
        'theta_std': np.std(theta),
        'alpha_mean': np.mean(alpha),
        'alpha_std': np.std(alpha),
        'beta_mean': np.mean(beta),
        'beta_std': np.std(beta),
        'theta_power': np.sum(theta ** 2) / len(theta),
        'alpha_power': np.sum(alpha ** 2) / len(alpha),
        'beta_power': np.sum(beta ** 2) / len(beta),
    }

    return features
