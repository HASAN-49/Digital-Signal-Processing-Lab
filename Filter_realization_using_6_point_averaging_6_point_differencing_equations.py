import numpy as np
import matplotlib.pyplot as plt

# Sample signal
n = np.arange(500)
m = np.arange(500)
x = np.sin(0.1 * np.pi * n) + 0.5 * np.random.randn(500)  # Sine wave + noise
# x = np.sin(0.1 * np.pi * n) + 0.5 * np.sin(0.1 * np.pi * m)  # Sine wave + noise

# 6-point Averaging Filter
def averaging_filter(signal):
    kernel = np.ones(6) / 6
    return np.convolve(signal, kernel, mode='same')

# 6-point Differencing Filter (simple alternating difference)
def differencing_filter(signal):
    kernel = np.array([1, -1, 1, -1, 1, -1]) / 6
    return np.convolve(signal, kernel, mode='same')

# Apply filters
y_avg = averaging_filter(x)
y_diff = differencing_filter(x)

# Plotting
plt.figure(figsize=(12, 6))

plt.subplot(3, 1, 1)
plt.plot(n, x, label='Original Signal')
plt.title('Original Signal')
plt.grid()

plt.subplot(3, 1, 2)
plt.plot(n, y_avg, color='green', label='6-Point Averaged')
plt.title('6-Point Averaging Filter Output (Low-Pass)')
plt.grid()

plt.subplot(3, 1, 3)
plt.plot(n, y_diff, color='red', label='6-Point Differenced')
plt.title('6-Point Differencing Filter Output (High-Pass)')
plt.grid()

plt.tight_layout()
plt.show()
