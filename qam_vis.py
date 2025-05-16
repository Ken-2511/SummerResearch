import numpy as np
import matplotlib.pyplot as plt

# User input values (can be changed or made interactive)
I0 = 1
I1 = -1
Q0 = 1
Q1 = -1

steps = 500
T = 2 * np.pi  # Only one period
omega = 1

t = np.linspace(0, T, steps + 1)

# QAM: I in {1, -1}, Q in {1, -1, 3, -3}
combinations = [
    (I, Q)
    for I in [1, -1]
    for Q in [1, -1, 3, -3]
]
titles = [f'I={I}, Q={Q}' for (I, Q) in combinations]

fig, axs = plt.subplots(2, 4, figsize=(20, 8))

for idx, ((I0, Q0), title) in enumerate(zip(combinations, titles)):
    row, col = divmod(idx, 4)
    I = np.full_like(t, I0)
    Q = np.full_like(t, Q0)
    iWave = I * np.cos(omega * t)
    qWave = Q * np.sin(omega * t)
    sumWave = iWave + qWave
    ax = axs[row, col]
    ax.plot(t, iWave, label='I(t)cos(wt)', color='blue', linewidth=1)
    ax.plot(t, qWave, label='Q(t)sin(wt)', color='red', linewidth=1)
    ax.plot(t, sumWave, label='Sum (QAM signal)', color='green', linewidth=2)
    ax.set_xlabel('Time (t)')
    ax.set_ylabel('Amplitude')
    ax.set_title(title, fontsize=12)
    ax.set_ylim([-4, 4])
    ax.legend(fontsize=8)
    ax.grid(True)

plt.tight_layout()
plt.show()
