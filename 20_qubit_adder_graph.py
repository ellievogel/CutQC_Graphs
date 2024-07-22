from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

# Data for adder with one node, 64 cores
data = [
    {
        'x': np.array([22,	24,	26,	28,	30,	32]),
        'y': np.array([1.30E+00,	3.26E+00,	9.51E+00,	3.54E+01,	1.42E+02,	2238.550362]),
        'label': 'Single-Node, Multi-Threaded'
    },
    {
        'x': np.array([22,	24,	26,	28,	30,	32]),
        'y': np.array([1.32E+01,	1.21E+01,	1.22E+01,	1.29E+01,	1.53E+01,	21.38172532]),
        'label': '8-GPU'
    },
]

plt.figure(Path(__file__).name)

# Set colors
colors = ['blue', 'orange']

# Plot each line with its specific x and y coordinates
for i, entry in enumerate(data):
    plt.scatter(entry['x'], entry['y'], color=colors[i], label=entry['label'])
    plt.plot(entry['x'], entry['y'], color=colors[i], linestyle='--')

# Add legend and labels
plt.legend()
plt.title('Adder')
plt.xlabel('Number of Qubits')
plt.ylabel('Compute Time (s)')
plt.yscale('log')

# Show plot
plt.show()
