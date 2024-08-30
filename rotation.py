#Aim- Transformation of complex numbers as 2-D vectors by rotation

import numpy as np 
import matplotlib.pyplot as git
import cmath

#Define the function
def rotate(z,angle):
    return z*np.exp(1j*cmath.pi*angle/180)
z=1+1j
angle=45
rotated_z=rotate(z,angle)

#Find the length of these two lines
original_length = abs(z)
rotated_length = abs(rotated_z)

# Check the length of these two lines in same or not
if original_length == rotated_length:
    print(f'length of orig_comp={round(original_length,4)}, length of rota_comp={round(rotated_length,4)}')
    print('Both length is same')
else:
    print('The length of these lines is not same')


'''
The angle between these two lines,
theta=arccos(real(original)*real(rotate)+imag(original)*imag(rotate)/|original|*|rotate|)*180/pi {degrees}
'''

# Find the angle between these two lines
dot_pro=z.imag*rotated_z.imag+z.real*rotated_z.real
cos_theta=dot_pro/(original_length*rotated_length)
angle_bet=np.arccos(cos_theta)*180/np.pi # Make the angle in degress
print(f'The angle between the original and rotated lines is {round(angle_bet,2)} degrees')


# Plotting the Lines
git.plot([0,z.real],[0,z.imag],label='Original')
git.plot([0,rotated_z.real],[0,rotated_z.imag],label='Rotated')

# PLotting the arc
angles=np.linspace(0,angle,100)
arc_points=z*np.exp(1j*np.pi*angles/180)
git.plot(arc_points.real,arc_points.imag)

git.gca().set_aspect('equal', adjustable='box')
git.grid()
git.legend()
git.xlabel('Real Part')
git.ylabel('Imaginary Part')
git.title('Rotation of a complex number')
git.legend()
git.show() 