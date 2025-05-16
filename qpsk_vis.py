import numpy as np
import matplotlib.pyplot as plt

steps = 500
T = 4 * np.pi
omega = 1

t = np.linspace(0, T, steps + 1)

# QPSK: Only two levels for I and Q, and they switch at half the period
# Four possible symbol combinations: (I, Q) = (1, 1), (1, -1), (-1, 1), (-1, -1)
# We'll plot all four in a 2x2 grid
combinations = [
    (1, 1),
    (1, -1),
    (-1, 1),
    (-1, -1)
]
titles = [f'I={I}, Q={Q}' for (I, Q) in combinations]

fig, axs = plt.subplots(2, 2, figsize=(12, 8))

for idx, ((I_val, Q_val), title) in enumerate(zip(combinations, titles)):
    row, col = divmod(idx, 2)
    # For QPSK, I and Q are constant for the whole symbol period
    iWave = I_val * np.cos(omega * t)
    qWave = Q_val * np.sin(omega * t)
    sumWave = iWave + qWave
    ax = axs[row, col]
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
