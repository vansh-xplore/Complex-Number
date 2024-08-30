import matplotlib.pyplot as plt

# Original square vertices as complex numbers
v1 = 0 + 0j
v2 = 1 + 0j
v3 = 1 + 1j
v4 = 0 + 1j

# Translation vector as a complex number
translation = 2 + 1j

# Apply the translation to each vertex
v1_translated = v1 + translation
v2_translated = v2 + translation
v3_translated = v3 + translation
v4_translated = v4 + translation

# Calculate the side length of original square
side_length=abs(v2-v1)

# Calculate the side length of translated square
side_length_translated=abs(v2_translated-v1_translated)

# Calculate the area of original and translated square 
area_original=side_length**2
area_translated=side_length_translated**2

# Check the areas are the same 
if area_original == area_translated: 
    print(f'The area are the same. Area: {area_original}')
else: 
    print('The area are different')

# Plotting the original square
plt.plot([v1.real, v2.real], [v1.imag, v2.imag], 'bo-')
plt.plot([v2.real, v3.real], [v2.imag, v3.imag], 'bo-')
plt.plot([v3.real, v4.real], [v3.imag, v4.imag], 'bo-')
plt.plot([v4.real, v1.real], [v4.imag, v1.imag], 'bo-', label='Original Square')

# Plotting the translated square
plt.plot([v1_translated.real, v2_translated.real], [v1_translated.imag, v2_translated.imag], 'ro-')
plt.plot([v2_translated.real, v3_translated.real], [v2_translated.imag, v3_translated.imag], 'ro-')
plt.plot([v3_translated.real, v4_translated.real], [v3_translated.imag, v4_translated.imag], 'ro-')
plt.plot([v4_translated.real, v1_translated.real], [v4_translated.imag, v1_translated.imag], 'ro-', label='Translated Square')

# Plotting grey lines connecting original and translated vertices
plt.plot([v1.real, v1_translated.real], [v1.imag, v1_translated.imag], color='grey')
plt.plot([v2.real, v2_translated.real], [v2.imag, v2_translated.imag], color='grey')
plt.plot([v3.real, v3_translated.real], [v3.imag, v3_translated.imag], color='grey')
plt.plot([v4.real, v4_translated.real], [v4.imag, v4_translated.imag], color='grey')

# Configure the plot
plt.legend()
plt.grid(True)
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.title('Translation of a Square using Complex Numbers')
plt.axis('equal')
plt.show()