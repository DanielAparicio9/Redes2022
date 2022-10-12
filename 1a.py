#--------------------------Librerias--------------------------------------------
import numpy as np
import scipy as sp
import scipy.linalg as linalg
import matplotlib.pyplot as plt
#------------------------------------------------------------------------------

#------------------------Condiciones Iniciales--------------------------------
E = -65 #mV
tau = 10 #ms
V0 =10 #mV
V1 =-130 #mV
#-----------------------------------------------------------------------------

#----------------------------Solución Analitica--------------------------------
def V(t,p):
    return E+(p-E)*np.exp(-t/tau)
#-----------------------------------------------------------------------------

#------------------------------Grafica-----------------------------------------
valores_t=np.linspace(0,100,100)
valores_V=np.vectorize(V)(valores_t,V0)
valores_V1=np.vectorize(V)(valores_t,V1)
plt.xlabel('$t$ [ms]')
plt.ylabel('$V(t)$ [mV]')
plt.plot(valores_t,valores_V,label="",linestyle='-',c='blue')
plt.plot(valores_t,valores_V1,label="",linestyle='-',c='red')
plt.plot(valores_t,np.zeros(len(valores_t)),label="",linestyle='--',c='gray')
plt.plot(valores_t,E*np.ones(len(valores_t)),label="$E=V^*$",linestyle='--',c='yellow')
plt.title('Integrate and Fire: Sin Disparo Ni Corriente')
plt.legend()
plt.show()
#-----------------------------------------------------------------------------


#----------------------------Función------------------------------------------
def f(V):
    return (E-V)/tau
#-----------------------------------------------------------------------------

#---------------------------------Grafica-------------------------------------
Vfix=E
valores_V=np.linspace(-120,20,100)
valores_f=np.vectorize(f)(valores_V)
plt.plot(valores_V,valores_f,label="",linestyle='-',c='red')
plt.plot(valores_V,np.zeros(len(valores_V)),label="",linestyle='--',c='gray') 
plt.plot([Vfix,Vfix],[-8,8],label="$V^*=E$",linestyle='--',c='cyan')
plt.arrow(Vfix-20.0,0.0,10.0,0.0,head_width=0.5,head_length=2,fc='g',ec='g')
plt.arrow(Vfix+20.0,0.0,-10.0,0.0,head_width=0.5,head_length=2,fc='g',ec='g')
plt.scatter([Vfix],[0],c='black')#circulo
plt.title('Integrate and Fire: sin disparo ni corriente')
plt.xlabel('$V$ [mV]')
plt.ylabel('$dV/dt=f(V)$ [mV/ms]')
plt.legend()
plt.show()
#----------------------------------------------------------------------------

