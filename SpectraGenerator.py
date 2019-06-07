import numpy as np
from numpy import *
from scipy import signal
import matplotlib.pyplot as plt
import os

'''
This program takes the inputs (Time Histories in txt files) to calculate
the spectra for 5% damping and plot them and save them in specific Directory
Have all the txt file for THs, DBE, and MCE in a specific folder
'''
def spect(Acc, dt):  # acc is in in/s2, dt is the time step
    Tn=0.05
    zeta=0.05
    m=1
    u_1=0
    Ax=[]
    PI=3.14159265359
    for i in range (795):
        wn=2*PI/Tn
        u=[0]
        for j in range (len(Acc)):
           if j==0:
               khat=1/(dt**2)+wn*zeta/(dt)
               a=1/(dt**2)- wn*zeta/(dt)
               b=(wn**2)-2/(dt**2)
               phat=(386*Acc[j]-a*u_1-b*u[j])
               u.append(phat/khat)
               
           else:
               phat=386*Acc[j]-a*u[j-1]-b*u[j]
               u.append(phat/khat)
        Tn += 0.01
        an=np.multiply((wn**2), u)
        Ax.append(max(np.absolute(an))/386)        
    return Ax

class loadData(object):
    def __init__ (self, directory, THx, THy,MCE, DBE, skip_header, factor):
        self.directory=directory
        self.THx=THx
        self.THy=THy
        self.MCE=MCE
        self.DBE=DBE
        self.skip_header=skip_header
        self.factor=factor
        self.datax=np.genfromtxt(self.directory+'/'+self.THx+'.txt', skip_header=self.skip_header)
        self.datay=np.genfromtxt(self.directory+'/'+self.THy+'.txt', skip_header=self.skip_header)
    
    def Spectra(self):
        Ax=spect(self.datax[:,1], self.datax[2,0]-self.datax[1,0])
        Ay=spect(self.datay[:,1], self.datay[2,0]-self.datay[1,0])
        d=[np.multiply(self.factor, Ax), np.multiply(self.factor,Ay)]
        Srss=np.sqrt(np.sum(np.square(d), axis=0))
        freqs=Srss
        t=np.linspace(0.05,8,795)
        return [d[0],d[1], freqs, t]
        
