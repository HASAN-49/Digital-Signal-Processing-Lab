import numpy as np
import matplotlib.pyplot as plt

# Analog signal parameters
A = 3
f = 50  # Hz
#Nyquist Rate = 2 * f
omega = 2 * np.pi * f  # 100π rad/s

# Sampling at 200 Hz
fs1 = 200
Ts1 = 1/fs1
n1 = np.arange(0, 40)  # 40 samples
t1 = n1 * Ts1  # Time instants
x1 = A * np.cos(omega * t1)  # Sampled signal

# Plot
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.stem(n1, x1, 'b', markerfmt='bo', basefmt=" ")
plt.title('Sampling at 200 Hz (Above Nyquist Rate)')
plt.xlabel('Sample index n')
plt.ylabel('x[n]')
plt.grid(True)

# Show corresponding analog signal for comparison
t_analog = np.linspace(0, 40*Ts1, 1000)
x_analog = A * np.cos(omega * t_analog)
plt.plot(t_analog/Ts1, x_analog, 'r--', alpha=0.5)
plt.legend(['Analog signal', 'Samples'])

# Sampling at 75 Hz
fs2 = 75
Ts2 = 1/fs2
n2 = np.arange(0, 15)  # 15 samples
t2 = n2 * Ts2  # Time instants
x2 = A * np.cos(omega * t2)  # Sampled signal

# Plot
plt.subplot(2, 1, 2)
plt.stem(n2, x2, 'g', markerfmt='go', basefmt=" ")
plt.title('Sampling at 75 Hz (Below Nyquist Rate)')
plt.xlabel('Sample index n')
plt.ylabel('x[n]')
plt.grid(True)

# Show corresponding analog signal for comparison
t_analog = np.linspace(0, 15*Ts2, 1000)
x_analog = A * np.cos(omega * t_analog)
plt.plot(t_analog/Ts2, x_analog, 'r--', alpha=0.5)
plt.legend(['Analog signal', 'Samples'])

plt.tight_layout()
plt.show()
