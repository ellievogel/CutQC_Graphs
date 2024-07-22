from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

# Data for bv with one node, 64 cores
data = [
    {
        'x': np.array([22,	24,	26,	28,	30,	32]),
        'y': np.array([0.09899383085,	9.47E-02,	1.91E-01,	5.92E-01,	1.93E+00,	13.5706435]),
        'label': 'Single-Node, Multi-Threaded'
    },
    {
        'x': np.array([22,	24,	26,	28,	30,	32]),
        'y': np.array([]),
        'label': '8-GPU'
    },
]

plt.figure(Path(__file__).name)

# Set colors
colors = ['purple', 'orange']

# Plot each line with its specific x and y coordinates
for i, entry in enumerate(data):
    plt.scatter(entry['x'], entry['y'], color=colors[i], label=entry['label'])
    plt.plot(entry['x'], entry['y'], color=colors[i], linestyle='--')

# Add legend and labels
plt.legend()
plt.title('BV')
plt.xlabel('Number of Qubits')
plt.ylabel('Compute Time (s)')
plt.yscale('log')

# Show plot
plt.show()
