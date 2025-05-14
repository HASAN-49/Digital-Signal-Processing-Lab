import numpy as np
import matplotlib.pyplot as plt

# Time axis
n = np.arange(-10, 11)  # from -10 to 10

## 1. Unit Step Sequence
def unit_step(n, n0=0):
    return np.where(n >= n0, 1, 0)

u = unit_step(n, 0)

plt.figure(figsize=(10, 6))
plt.subplot(2, 3, 1)
plt.stem(n, u)
plt.title('Unit Step Sequence')
plt.xlabel('n')
plt.ylabel('u[n]')

## 2. Ramp Sequence
def ramp(n, n0=0):
    return np.where(n >= n0, n - n0, 0)

r = ramp(n, 0)

plt.subplot(2, 3, 2)
plt.stem(n, r)
plt.title('Ramp Sequence')
plt.xlabel('n')
plt.ylabel('r[n]')

## 3. Exponential Sequence
a = 0.9  # can be any real number
exp_seq = a**n

plt.subplot(2, 3, 3)
plt.stem(n, exp_seq)
plt.title('Exponential Sequence (a=0.9)')
plt.xlabel('n')
plt.ylabel('a^n')

## 4. Sine Sequence
f = 0.05  # frequency
n = np.arange(-15, 16)
sine_seq = np.sin(2 * np.pi * f * n)

plt.subplot(2, 3, 4)
plt.stem(n, sine_seq)
plt.title('Sine Sequence (f=0.1)')
plt.xlabel('n')
plt.ylabel('sin(2πfn)')

## 5. Cosine Sequence
cos_seq = np.cos(2 * np.pi * f * n)

plt.subplot(2, 3, 5)
plt.stem(n, cos_seq)
plt.title('Cosine Sequence (f=0.1)')
plt.xlabel('n')
plt.ylabel('cos(2πfn)')

plt.tight_layout()
plt.show()
