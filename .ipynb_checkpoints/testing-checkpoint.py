import matplotlib.pyplot as plt
import numpy as np

# Generate sample data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(2 * x)
y4 = np.cos(2 * x)

# Create a figure with subplots
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# Plot on the first subplot
axs[0, 0].plot(x, y1, color='blue', label='sin(x)')
axs[0, 0].set_title('Plot 1')
axs[0, 0].legend()

# Plot on the second subplot
axs[0, 1].plot(x, y2, color='green', label='cos(x)')
axs[0, 1].set_title('Plot 2')
axs[0, 1].legend()

# Plot on the third subplot
axs[1, 0].plot(x, y3, color='red', label='sin(2x)')
axs[1, 0].set_title('Plot 3')
axs[1, 0].legend()

# Plot on the fourth subplot
axs[1, 1].plot(x, y4, color='purple', label='cos(2x)')
axs[1, 1].set_title('Plot 4')
axs[1, 1].legend()

# Adjust layout for better spacing
plt.tight_layout()

# Show the plots
plt.show()