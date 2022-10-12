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
#-------------------------------------------------------------------------------------


#--------------------Función Rk4----------------------------------------
def rk4(f,x,t,h,p):
    k1 = f(x,t,p)
    k2 = f(x+0.5*h*k1,t+0.5*h,p)
    k3 = f(x+0.5*h*k2,t+0.5*h,p)
    k4 = f(x+h*k3,t+h,p)
    return h*(k1+2.0*k2+2.0*k3+k4)/6.0
#-----------------------------------------------------------------------

#--------------------------------Función con Corriente Independiente del Tiempo--------------------------
def V(t,v,p):
    return (1/tau)*(E-v+R*Ie)
#------------------------------------------------------------------------------------------------------

#-----------------------Condiciones Iniciales------------------------------------------------------------
h=0.05 #ms
t = np.zeros(4001)
v1 = np.zeros(len(t))
t[0]=0#s
v1[0]=V0
k=4000
j=0
#-------------------------------------------------------------------------------------------------------

#----------------------------------------Simulación---------------------------------------------------
for i in range(k): 
    v1[i+1]=v1[i]+rk4(V,t[i],v1[i],h,1)
    t[i+1]=t[i]+h
    j=j+h
    if v1[i+1]>=-50:
        v1[i+1]=-65
        print(j,1/j)
        j=0
#-----------------------------------------------------------------------------------------------------

#---------------------------------------Grafica--------------------------------------------------------
plt.plot(t,v1,label="V(t)",linestyle='-',c='blue')
plt.plot([0,200],[-50,-50],label="Umbral",linestyle='--',c='yellow')
plt.title('Integrate and Fire: Con Disparo y Corriente')
plt.legend()
plt.xlabel('$t$ [ms]')
plt.ylabel('$V(t)$ [mV]')
plt.show()
#-----------------------------------------------------------------------------------------------------