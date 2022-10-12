#--------------------------Librerias--------------------------------------------
import numpy as np
import scipy as sp
import scipy.linalg as linalg
import matplotlib.pyplot as plt
import math
#------------------------------------------------------------------------------


#---------------------------------Valores Iniciales------------------------------------
tau = 10 #ms
E = -65 #mV
R=10 #Mohm
Ie=2#nA
V0 = -65 #mV
Vu=-50
#-------------------------------------------------------------------------------------

# Corriente crítica.
Ic = (Vu-E)/R

def periodo(I0):
    return tau*np.log(I0*R/(I0*R+E-Vu))    
def frecuencia(I0):
    return 1/periodo(I0)

valores_I0 = np.linspace(Ic+0.01,2*Ic,10)
print(frecuencia(2))
plt.xlabel('$I_0$ [nA]')
plt.ylabel('frecuencia [1/ms]')
plt.scatter(np.linspace(0,Ic,10),np.zeros(10),label="",linestyle='--',c='blue')#Debajo corriente critica
plt.scatter(valores_I0,np.vectorize(frecuencia)(valores_I0),label="",linestyle='--',c='blue')#Por encima corriente critica
plt.title('Integrate and Fire: frecuencia de disparo')
#plt.legend() 
plt.show()   