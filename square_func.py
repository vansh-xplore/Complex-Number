import numpy as np
import matplotlib.pyplot as plt

# Define the circular arc in polar coordinates
theta = np.linspace(0, np.pi / 2, 100)  # Angle range
r = 1  # Radius of the circular arc

# Convert to complex numbers (z = r * e^(i*theta))
z = r * np.exp(1j * theta)

# Apply the z^2 mapping
w = z**2

# Plotting in polar coordinates
fig,axes=plt.subplots(1,2,figsize=(12,6))
# Original circular arc
axes[0].plot(z.real,z.imag, label='θ∈(0,π/2)', color='blue')
axes[0].set_title('Original Circular Arc')
axes[0].set_xlabel('Real Part')
axes[0].set_ylabel('Imaginary Part')
axes[0].grid(True)
axes[0].legend()

# Image of the circular arc under z^2 mapping
axes[1].plot(w.real,w.imag, label='θ∈(0,π)', color='red')
axes[1].set_title('Image under z^2 Mapping')
axes[1].set_xlabel('Real Part')
axes[1].set_ylabel('Imaginary Part')
axes[1].grid(True)
axes[1].legend()

plt.suptitle('Mapping of f(z)=z**2 for θ∈(0,π/2)')
plt.tight_layout()
plt.show()