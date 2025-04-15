import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import chirp, square, sawtooth, unit_impulse

# Parametry sygnału
fs = 1000  # Częstotliwość próbkowania (Hz)
t = np.linspace(0, 1, fs, endpoint=False)  # Oś czasu 1 sekunda

# a) Sygnał sinusoidalny
sin_wave = np.sin(2 * np.pi * 5 * t)  # 5 Hz

# b) Sygnał prostokątny
square_wave = square(2 * np.pi * 5 * t)  # 5 Hz

# c) Sygnał piłokształtny
sawtooth_wave = sawtooth(2 * np.pi * 5 * t)  # 5 Hz

# d) Sygnał świergotliwy (chirp)
chirp_wave = chirp(t, f0=5, f1=50, t1=1, method='linear')

# e) Superpozycja sinusa i cosinusa
superposition_wave = np.sin(2 * np.pi * 5 * t) + 0.5 * np.cos(2 * np.pi * 10 * t)

# f) Impuls jednostkowy
impulse_wave = unit_impulse(fs, idx=fs//2)

# Tworzenie wykresów
fig, axes = plt.subplots(3, 2, figsize=(12, 8))

# Rysowanie sygnałów
axes[0, 0].plot(t, sin_wave)
axes[0, 0].set_title("Sinus")

axes[0, 1].plot(t, square_wave)
axes[0, 1].set_title("Prostokątny")

axes[1, 0].plot(t, sawtooth_wave)
axes[1, 0].set_title("Piłokształtny")

axes[1, 1].plot(t, chirp_wave)
axes[1, 1].set_title("Świergotliwy")

axes[2, 0].plot(t, superposition_wave)
axes[2, 0].set_title("Superpozycja sinus + cosinus")

axes[2, 1].plot(t, impulse_wave)
axes[2, 1].set_title("Impuls jednostkowy")

# Ustawienia wykresów
for ax in axes.flat:
    ax.set_xlim(0, 1)
    ax.grid(True)

plt.tight_layout()
plt.show()


df = pd.DataFrame({'Time': t, 'Signal': chirp_wave})
df.to_csv('signal.csv', index=False)