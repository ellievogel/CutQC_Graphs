from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

# Data for adder with one node, 64 cores
data = [
    {
        'x': np.array([22,	24,	26,	28,	30,	32,	34]),
        'y': np.array([1.10E-01,	1.40E-01,	3.21E-01,	1.03E+00,	3.48E+00, 0, 0]),
        'label': 'Single-Node, Multi-Threaded'
    },
    # {
    #     'x': np.array([12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32]),
    #     'y': np.array([18.98123212,	18.91318715,	18.9852025,	19.61403576,	54.73860591,	56.10556875,	44.24588567,	45.85792219,	91.30829361,	154.6123012,	154.946389]),
    #     'label': 'Multi-Node'
    # },
    # {
    #     'x': np.array([12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32]),
    #     'y': np.array([21.10670842,	20.9216488,	20.97864509,	21.46630783,	59.93718648,	61.81656588,	61.56445743,	65.38468128,	118.9313233,	148.8722855,	246.297376]),
    #     'label': 'Multi-GPU'
    # }
]

plt.figure(Path(__file__).name)

# Set colors
colors = plt.cm.viridis(np.linspace(0, 1, len(data)))

# Plot each line with its specific x and y coordinates
for i, entry in enumerate(data):
    plt.scatter(entry['x'], entry['y'], color=colors[i], label=entry['label'])
    plt.plot(entry['x'], entry['y'], color=colors[i], linestyle='--')

# Add legend and labels
plt.legend()
plt.title('Adder')
plt.xlabel('Size of circuit')
plt.ylabel('Build Time')
plt.yscale('log')

# Show plot
plt.show()
