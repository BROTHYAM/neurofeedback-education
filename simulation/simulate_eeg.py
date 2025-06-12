"""
EEG Signal Simulation Script

This script simulates synthetic EEG signals representing three common brainwave types:
Alpha (10 Hz), Beta (20 Hz), and Theta (6 Hz). It adds Gaussian noise to simulate the
natural variability of EEG data. The focus is on highlighting the Beta wave, which is
typically associated with attention and active concentration in neurofeedback applications.
"""

import numpy as np
import matplotlib.pyplot as plt

# EEG simulation function
def simulate_eeg_waves(sim_time, sampling_rate=250):
    """
    Simulates alpha, beta, and theta EEG waves with added Gaussian noise.

    Parameters:
        sim_time (float): Duration of the signal in seconds.
        sampling_rate (int): Number of samples per second.

    Returns:
        t (np.ndarray): Time vector.
        alpha (np.ndarray): Alpha wave signal (10 Hz).
        beta (np.ndarray): Beta wave signal (20 Hz) — related to concentration.
        theta (np.ndarray): Theta wave signal (6 Hz).
    """
    t = np.linspace(0, sim_time, int(sim_time * sampling_rate))

    # Simulated EEG signals with added Gaussian noise
    alpha = np.sin(2 * np.pi * 10 * t) + np.random.normal(0, 0.3, len(t))   # Relaxation
    beta = np.sin(2 * np.pi * 20 * t) + np.random.normal(0, 0.3, len(t))    # Attention
    theta = np.sin(2 * np.pi * 6 * t) + np.random.normal(0, 0.3, len(t))    # Drowsiness

    return t, alpha, beta, theta

# Run the simulation for 10 seconds (or any desired duration)
duration = 10
t, alpha, beta, theta = simulate_eeg_waves(duration)

# Plotting EEG waves
plt.figure(figsize=(12, 8))

# Alpha wave
plt.subplot(3, 1, 1)
plt.plot(t, alpha, label='Alpha Wave (10 Hz)', color='gray')
plt.title('Alpha Wave (10 Hz) – Calm, Eyes Closed')
plt.ylabel('Amplitude (uV)')

# Beta wave (highlighted for focus)
plt.subplot(3, 1, 2)
plt.plot(t, beta, label='Beta Wave (20 Hz)', color='red')
plt.title('Beta Wave (20 Hz) – Attention and Concentration')  # <- Emphasis here
plt.ylabel('Amplitude (uV)')

# Theta wave
plt.subplot(3, 1, 3)
plt.plot(t, theta, label='Theta Wave (6 Hz)', color='green')
plt.title('Theta Wave (6 Hz) – Drowsiness or Light Sleep')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude (uV)')

plt.tight_layout()
plt.show()
