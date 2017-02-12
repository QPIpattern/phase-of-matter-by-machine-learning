#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 11:02:10 2017

@author: kris
"""
import matplotlib
#matplotlib.use('Agg')
import numpy as np
from numpy import linalg as LA
import matplotlib.pyplot as plt
import time
L = 32
#plot the figures
#T = np.linspace(0.1, 2.5, 20)
ms=np.loadtxt('data/output_measures.dat')
T,E,SpcH,M,M_sus=ms[:,0],ms[:,1],ms[:,2],ms[:,3],ms[:,4]
plt.figure()
plt.plot(T, E, 'rx-')
plt.xlabel(r'Temperature $(\frac{J}{k_B})$')
plt.ylabel(r'$\langle E \rangle$ per site $(J)$')
plt.savefig("E.pdf", format='pdf', bbox_inches='tight')

plt.figure()
plt.plot(T, SpcH, 'kx-')
plt.xlabel(r'Temperature $(\frac{J}{k_B})$')
plt.ylabel(r'$C_V$ per site $(\frac{J^2}{k_B^2})$')
plt.savefig("Cv.pdf", format='pdf', bbox_inches='tight')

plt.figure()
plt.plot(T, M, 'bx-')
plt.xlabel(r'Temperature $(\frac{J}{k_B})$')
plt.ylabel(r'$\langle|M|\rangle$ per site $(\mu)$')
plt.savefig("M.pdf", format='pdf', bbox_inches='tight')

plt.figure()
plt.plot(T, M_sus, 'gx-')
plt.xlabel(r'Temperature $(\frac{J}{k_B})$')
plt.ylabel(r'$\chi$ $(\frac{\mu}{k_B})$')
plt.savefig("chi.pdf", format='pdf', bbox_inches='tight')

plt.tight_layout()
fig = plt.gcf()
plt.show()