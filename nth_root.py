import cmath 
import numpy as np 
import matplotlib.pyplot as plt 

def nth_root(z,n):
    r,theta=cmath.polar(z)
    omega=r**(1/n)
    roots=[]
    argument=[]

    for i in range(n): 
        # Argument of each root
        phi=(theta+2*np.pi*i)/n 

        root_magintude=omega
        root_argument=phi

        # Root in Cartesian form
        root_cartesain=cmath.rect(root_magintude,root_argument)
        roots.append(root_cartesain)
        argument.append(root_argument)

        print(f'Root {i}:')
        print(f'In Polar form: Magnitude= {root_magintude}, Angle={root_argument} radians')
        print(f'In cartesian form: Root={root_cartesain}')

    return roots, argument, omega 

# Parameters
z=3+4j
n=5

# Radius is root_magnitude (Magnitude)
roots,argument, radius=nth_root(z,n)

print('')

plt.figure(figsize=(6,6))

for i in range(n): 
    print(f'Argument of {i}th root in degrees is ({np.degrees(argument[i])})')
    
    root=roots[i]
    # Line from origin to root
    plt.plot([0,root.real],[0,root.imag])

    arg_deg=np.degrees(argument[i])
    plt.scatter(root.real,root.imag,label=f'{i}-th root')
    plt.text(root.real,root.imag,f'θ={np.degrees(argument[i]):.2f}°')

angles=np.linspace(0,2*np.pi,100)
circle_x=radius*np.cos(angles)
circle_y=radius*np.sin(angles)

plt.xlim(-2,2)
plt.ylim(-2,2)

#Plot the circle
plt.plot(circle_x,circle_y,color='green')

plt.axhline(0,color='black',linewidth=0.5,linestyle='dashdot')
plt.axvline(0,color='black',linewidth=0.5,linestyle='dashdot')

plt.grid(linewidth=0.5,linestyle='dashdot')

plt.title(f'All {n}th Roots of {z}')
plt.xlabel('Real Part')
plt.ylabel('Imaginary Part')
plt.legend()

plt.show()