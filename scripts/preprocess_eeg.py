"""
preprocess_eeg.py

This script provides basic preprocessing functions for EEG signals,
including bandpass filtering to isolate relevant frequency bands,
removal of powerline noise using a notch filter, and normalization.

Author: [Tu Nombre]
Date: 2025-06-12
"""

import numpy as np
from scipy.signal import butter, filtfilt, iirnotch


def bandpass_filter(data, lowcut, highcut, fs, order=5):
    """
    Apply a Butterworth bandpass filter to EEG data.

    Parameters:
    - data (numpy array): Raw EEG signal.
    - lowcut (float): Low frequency cut-off (Hz).
    - highcut (float): High frequency cut-off (Hz).
    - fs (int): Sampling frequency (Hz).
    - order (int): Filter order.

    Returns:
    - filtered_data (numpy array): Bandpass filtered EEG signal.
    """
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq

    b, a = butter(order, [low, high], btype='band')
    filtered_data = filtfilt(b, a, data)
    return filtered_data


def notch_filter(data, fs, freq=50.0, quality=30.0):
    """
    Apply a notch filter to remove powerline noise (default 50 Hz).

    Parameters:
    - data (numpy array): EEG signal.
    - fs (int): Sampling frequency (Hz).
    - freq (float): Frequency to remove (Hz).
    - quality (float): Quality factor of the notch filter.

    Returns:
    - filtered_data (numpy array): EEG signal after notch filtering.
    """
    nyq = 0.5 * fs
    w0 = freq / nyq
    b, a = iirnotch(w0, quality)
    filtered_data = filtfilt(b, a, data)
    return filtered_data


def normalize_signal(data):
    """
    Normalize EEG signal to zero mean and unit variance.

    Parameters:
    - data (numpy array): EEG signal.

    Returns:
    - normalized_data (numpy array): Normalized EEG signal.
    """
    mean = np.mean(data)
    std = np.std(data)
    normalized_data = (data - mean) / std
    return normalized_data


if __name__ == "__main__":
    # Example usage with simulated data
    import matplotlib.pyplot as plt

    fs = 250  # Sampling frequency in Hz
    t = np.linspace(0, 10, fs*10)  # 10 seconds of data
    raw_signal = np.sin(2 * np.pi * 10 * t) + 0.5 * np.sin(2 * np.pi * 50 * t) + 0.3 * np.random.randn(len(t))

    # Remove powerline noise (50 Hz)
    notch_signal = notch_filter(raw_signal, fs)

    # Bandpass filter between 1 Hz and 40 Hz
    filtered_signal = bandpass_filter(notch_signal, 1, 40, fs)

    # Normalize
    normalized_signal = normalize_signal(filtered_signal)

    # Plot results
    plt.figure(figsize=(12, 8))
    plt.subplot(4, 1, 1)
    plt.plot(t, raw_signal)
    plt.title("Raw EEG Signal")
    plt.subplot(4, 1, 2)
    plt.plot(t, notch_signal)
    plt.title("After Notch Filter (50 Hz)")
    plt.subplot(4, 1, 3)
    plt.plot(t, filtered_signal)
    plt.title("After Bandpass Filter (1-40 Hz)")
    plt.subplot(4, 1, 4)
    plt.plot(t, normalized_signal)
    plt.title("Normalized Signal")
    plt.xlabel("Time (seconds)")
    plt.tight_layout()
    plt.show()
