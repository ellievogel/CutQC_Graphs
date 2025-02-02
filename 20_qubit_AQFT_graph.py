from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

# Data for adder with one node, 64 cores
data = [
    {
        'x': np.array([22,	24,	26,	28,	30,	32]),
        'y': np.array([1.10E-01,	1.40E-01,	3.21E-01,	1.03E+00,	3.48E+00,	19.61032261]),
        'label': 'Single-Node, Multi-Threaded'
    },
    {
        'x': np.array([22,	24,	26]),
        'y': np.array([2.24E+00,	2.24E+00,	1.28E+01]),
        'label': '8-GPU'
    },
]

plt.figure(Path(__file__).name)

# Set colors
colors = ['green', 'orange']

# Plot each line with its specific x and y coordinates
for i, entry in enumerate(data):
    plt.scatter(entry['x'], entry['y'], color=colors[i], label=entry['label'])
    plt.plot(entry['x'], entry['y'], color=colors[i], linestyle='--')

# Add legend and labels
plt.legend()
plt.title('AQFT')
plt.xlabel('Number of Qubits')
plt.ylabel('Compute Time (s)')
plt.yscale('log')

# Show plot
plt.show()
