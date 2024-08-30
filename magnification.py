import matplotlib.pyplot as plt
import numpy as np 

def magnification(z,m):
    z_magnified = z*m
    return z_magnified
z = 3+4j
m = 5
z_magnified = magnification(z,m)

# Plot the original and magnified complex numbers
r_original = np.abs(z)
theta_original = np.angle(z)
r_magnified = np.abs(z_magnified)
theta_magnified = np.angle(z_magnified)

# Plotting in polar coordinates
plt.figure(figsize=(10, 5))

# Original complex number
plt.subplot(1, 2, 1)
plt.plot([0, theta_original], [0, r_original], 'bo-', label='Original')
plt.title('Original Complex Number')
plt.grid()
plt.xlabel('Real Axis')
plt.ylabel('Imaginary Axes')

# Magnified complex number
plt.subplot(1, 2, 2)
plt.plot([0, theta_magnified], [0, r_magnified], 'ro-', label='Magnified')
plt.title('Magnified Complex Number')
plt.grid()
plt.xlabel('Real Axis')
plt.ylabel('Imaginary Axes')

plt.suptitle('Magnification of complex number')
plt.tight_layout()
plt.show()