from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

# Data for adder with one node, 64 cores
data = [
    {
        'x': np.array([24,	25,	30]),
        'y': np.array([0.8320163512,	5.163439431,	147.8112745]),
        'label': 'Single-Node, Multi-Threaded'
    },
    {
        'x': np.array([24,	25]),
        'y': np.array([12.47780728,	12.56886335]),
        'label': '8-GPU'
    },
]

plt.figure(Path(__file__).name)

# Set colors
colors = ['red', 'orange']

# Plot each line with its specific x and y coordinates
for i, entry in enumerate(data):
    plt.scatter(entry['x'], entry['y'], color=colors[i], label=entry['label'])
    plt.plot(entry['x'], entry['y'], color=colors[i], linestyle='--')

# Add legend and labels
plt.legend()
plt.title('Supremacy')
plt.xlabel('Number of Qubits')
plt.ylabel('Compute Time (s)')
plt.yscale('log')

# Show plot
plt.show()
