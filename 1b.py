#--------------------------Librerias--------------------------------------------
import numpy as np
import scipy as sp
import scipy.linalg as linalg
import matplotlib.pyplot as plt
#------------------------------------------------------------------------------

#------------------------Condiciones Iniciales--------------------------------
E = -65 #mV
tau = 10 #ms
V0 = -65 #mV
V1=0 #mV
R=10 #Mohm
Ie=2#nA
Vfix=E+R*Ie
#-----------------------------------------------------------------------------

#----------------------------Solución Analitica--------------------------------
def V(t,p):
    return (E+R*Ie)+(p-Vfix)*np.exp(-t/tau)#Podria usar Vfix
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
plt.plot(valores_t,(Vfix)*np.ones(len(valores_t)),label="$V^*=E+R*Ie$",linestyle='--',c='yellow')
plt.title('Integrate and Fire: sin disparo con corriente constante')
plt.legend()
plt.show()
#-----------------------------------------------------------------------------


#----------------------------Función------------------------------------------
def f(V):
    return (Vfix-V)/tau
#-----------------------------------------------------------------------------

#---------------------------------Grafica-------------------------------------
valores_V=np.linspace(-120,20,100)
valores_f=np.vectorize(f)(valores_V)
plt.plot(valores_V,valores_f,label="",linestyle='-',c='red') #grafica
plt.plot(valores_V,np.zeros(len(valores_V)),label="",linestyle='--',c='gray') #eje x
plt.plot([Vfix,Vfix],[-8,8],label="$V^*=E+R*Ie$",linestyle='--',c='cyan') #recta vertical
plt.arrow(Vfix-20.0,0.0,10.0,0.0,head_width=0.5,head_length=2,fc='g',ec='g')#flecha izq
plt.arrow(Vfix+20.0,0.0,-10.0,0.0,head_width=0.5,head_length=2,fc='g',ec='g') #flecha der
plt.scatter([Vfix],[0],c='black')#circulo
plt.title('Integrate and Fire: sin disparo con corriente constante')
plt.xlabel('$V$ [mV]')
plt.ylabel('$dV/dt=f(V)$ [mV/ms]')
plt.legend()
plt.show()
#----------------------------------------------------------------------------

