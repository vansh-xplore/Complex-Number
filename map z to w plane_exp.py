import numpy as np 
import matplotlib.pyplot as plt 

def f(z): 
    return np.exp(z)
k_values=np.array([-2,-1,0,1,2])
y=np.linspace(-10,10,400)
fig,axes=plt.subplots(1,2,figsize=(12,6))
for i in k_values: 
    z=i+1j*y
    axes[0].plot(np.real(z),np.imag(z),label=f'x={i}')
axes[0].set_title('Vertical Lines x=k in z-plane')
axes[0].set_xlabel('Real Part')
axes[0].set_ylabel('Imaginary Part')
axes[0].grid()
axes[0].legend()

for i in k_values: 
    z=i+1j*y 
    ω=f(z)
    axes[1].plot(np.real(ω),np.imag(ω),label=f'f(z) for x={i}')
axes[1].set_title('Images of the vertical lines in the ω graph')
axes[1].set_xlabel('Real Part')
axes[1].set_ylabel('Imaginary Part')
axes[1].grid()
axes[1].legend()

plt.suptitle('Mapping: f(z)=exp(z)')
plt.subplots_adjust()
plt.show()