import numpy as np
import matplotlib.pyplot as plt
from scipy import fft

steps = 500
T = 2 * np.pi  # Only one period
omega = 1

t = np.linspace(0, T, steps + 1)

# Four possible symbol combinations for QAM and QPSK
qam_combinations = [
    (1, 1),
    (1, -1),
    (-1, 1),
    (-1, -1)
]
qam_titles = [f'QAM: I={I0}, Q={Q0}' for (I0, Q0) in qam_combinations]
qpsk_combinations = [
    (1, 1),
    (1, -1),
    (-1, 1),
    (-1, -1)
]
qpsk_titles = [f'QPSK: I={I0}, Q={Q0}' for (I0, Q0) in qpsk_combinations]

fig, axs = plt.subplots(2, 4, figsize=(20, 8))

# QAM plots (first row)
for idx, ((I0, Q0), title) in enumerate(zip(qam_combinations, qam_titles)):
    I = np.full_like(t, I0)
    Q = np.full_like(t, Q0)
    iWave = I * np.cos(omega * t)
    qWave = Q * np.sin(omega * t)
    sumWave = iWave + qWave
    ax = axs[0, idx]
    ax.plot(t, iWave, label='I(t)cos(wt)', color='blue', linewidth=1)
    ax.plot(t, qWave, label='Q(t)sin(wt)', color='red', linewidth=1)
    ax.plot(t, sumWave, label='Sum (QAM signal)', color='green', linewidth=2)
    ax.set_xlabel('Time (t)')
    ax.set_ylabel('Amplitude')
    ax.set_title(title, fontsize=12)
    ax.legend(fontsize=8)
    ax.grid(True)

# QPSK plots (second row)
for idx, ((I0, Q0), title) in enumerate(zip(qpsk_combinations, qpsk_titles)):
    I = np.full_like(t, I0)
    Q = np.full_like(t, Q0)
    iWave = I * np.cos(omega * t)
    qWave = Q * np.sin(omega * t)
    sumWave = iWave + qWave
    ax = axs[1, idx]
    ax.plot(t, iWave, label='I*cos(wt)', color='blue', linewidth=1)
    ax.plot(t, qWave, label='Q*sin(wt)', color='red', linewidth=1)
    ax.plot(t, sumWave, label='QPSK signal', color='purple', linewidth=2)
    ax.set_xlabel('Time (t)')
    ax.set_ylabel('Amplitude')
    ax.set_title(title, fontsize=12)
    ax.legend(fontsize=8)
    ax.grid(True)

plt.tight_layout()
plt.show()

# Simulation parameters
fs = 1_000_000  # 1 MHz sampling rate
T = 0.01        # 10 ms total duration
N = int(fs * T)
t = np.arange(N) / fs

fc = 100_000    # 100 kHz carrier
fm = 1_000      # 1 kHz message

# Generate random bits for I and Q (simulate many symbols)
num_symbols = int(T * fm)
I_bits = np.random.choice([-1, 1], num_symbols)
Q_bits = np.random.choice([-1, 1], num_symbols)

# Upsample to match the time vector
samples_per_symbol = N // num_symbols
I = np.repeat(I_bits, samples_per_symbol)
Q = np.repeat(Q_bits, samples_per_symbol)
I = I[:N]
Q = Q[:N]

# Message signal (1 kHz sine)
msg = np.sin(2 * np.pi * fm * t)

# QAM: I and Q modulate carrier and quadrature
qam_signal = I * msg * np.cos(2 * np.pi * fc * t) + Q * msg * np.sin(2 * np.pi * fc * t)
# QPSK: I and Q modulate carrier and quadrature (no amplitude modulation)
qpsk_signal = I * np.cos(2 * np.pi * fc * t) + Q * np.sin(2 * np.pi * fc * t)

# Compute FFTs
qam_spectrum = np.abs(fft.fft(qam_signal))
qpsk_spectrum = np.abs(fft.fft(qpsk_signal))
freqs = fft.fftfreq(N, d=1/fs)

# Only plot positive frequencies
half = N // 2

fig, axs = plt.subplots(2, 1, figsize=(12, 8))

axs[0].plot(freqs[:half]/1e3, qam_spectrum[:half], color='green')
axs[0].set_title('QAM Spectrum (100kHz carrier, 1kHz message, random symbols)')
axs[0].set_xlabel('Frequency (kHz)')
axs[0].set_ylabel('Magnitude')
axs[0].grid(True)

axs[1].plot(freqs[:half]/1e3, qpsk_spectrum[:half], color='purple')
axs[1].set_title('QPSK Spectrum (100kHz carrier, random symbols)')
axs[1].set_xlabel('Frequency (kHz)')
axs[1].set_ylabel('Magnitude')
axs[1].grid(True)

plt.tight_layout()
plt.show()
