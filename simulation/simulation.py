import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la señal
fs = 256  # frecuencia de muestreo en Hz
duration = 10  # duración de la señal en segundos
t = np.linspace(0, duration, fs * duration, endpoint=False)

# Componentes EEG simuladas
delta = 0.5 * np.sin(2 * np.pi * 2 * t)      # 0.5–4 Hz
theta = 0.5 * np.sin(2 * np.pi * 6 * t)      # 4–8 Hz
alpha = 1.0 * np.sin(2 * np.pi * 10 * t)     # 8–12 Hz
beta = 0.3 * np.sin(2 * np.pi * 20 * t)      # 13–30 Hz
gamma = 0.1 * np.sin(2 * np.pi * 40 * t)     # 30–50 Hz

# Ruido blanco
noise = 0.5 * np.random.normal(size=len(t))

# Señal total
eeg_signal = delta + theta + alpha + beta + gamma + noise

# Opcional: simular evento breve (pico)
eeg_signal[fs*3:fs*3+fs//5] += 2 * np.hanning(fs//5)

# Graficar la señal simulada
plt.figure(figsize=(12, 4))
plt.plot(t, eeg_signal, label="EEG simulada")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud (uV)")
plt.title("Señal EEG simulada")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
