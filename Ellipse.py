#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 08:49:27 2021

@author: yvan
"""
import numpy as np
import matplotlib.pyplot as plt
import numpy.random as rnd
import config

##--------------------------------FONCTIONS----------------------------------##
def generate_ellipse_by_angles(t, C, a, b, theta, phi):
    n = np.array([np.cos(phi)*np.sin(theta), np.sin(phi)*np.sin(theta), np.cos(theta)])
    u = np.array([-np.sin(phi), np.cos(phi), 0])
    P_ellipse = a*np.cos(t)[:, np.newaxis]*u + b*np.sin(t)[:, np.newaxis]*np.cross(n, u) + C
    return P_ellipse

##------------------------------FIN FONCTIONS--------------------------------##

##-------------------------------CONSTANTES----------------------------------##

largeur_lim = config.largeur_lim
hauteur_lim = config.hauteur_lim
theta = np.pi*90/180
phi = 0
rayonH = config.rayonH
rayonV = config.rayonV
ecartH = config.ecartH
nbrows = int( (hauteur_lim-0.5e-3)/(4*rayonV+0.5e-3) )
nbcolumns = int( (largeur_lim-ecartH)/(2*rayonH+ecartH) )
nbelem = nbrows*nbcolumns

t = np.linspace(0, 2*np.pi, 50)
P_gen = np.zeros((nbelem, len(t), 3))

##------------------------------FIN CONSTANTES-------------------------------##

##--------------------------------ELLIPSES-----------------------------------##

#Creation du quadrillage
pos = np.zeros((nbelem, 3))
k = 0
for l in range(nbrows):
    for m in range(nbcolumns):
        pos[k,1] = m*largeur_lim/nbcolumns
        pos[k,2] = l*hauteur_lim/nbrows
        pos[k,0] = 0
        k = k+1

#Creation des ellipses à pos et demi grand axe vertical aléatoire
e=np.zeros((nbelem, len(t), 3))
for i in range(nbelem):
    e[i]=generate_ellipse_by_angles(t, pos[i], rayonH, rayonV*(1+rnd.rand()), theta, phi)
    
##------------------------------FIN ELLIPSES---------------------------------##

##--------------------------------AFFICHAGE----------------------------------##

fig = plt.figure(1, figsize=(largeur_lim/0.0254, hauteur_lim/0.0254))
#fig.set_size_inches(largeur_lim/0.0254, hauteur_lim/0.0254)

ax = fig.add_subplot(111, aspect='equal')
axe = plt.gca()
x_axis = axe.axes.get_xaxis()
x_axis.set_visible(False)
y_axis = axe.axes.get_yaxis()
y_axis.set_visible(False)
#axe.patch.set_visible(False)
#plt.scatter(pos[:,1], pos[:,2], marker='+', color='b')
for i in range(nbelem):
    plt.plot(e[i, :, 1], e[i, :, 2], color='black')
    ax.fill(e[i, :, 1], e[i, :, 2], 'k',zorder=10)
plt.xlim(0-rayonH*2, largeur_lim)
plt.ylim(0-2*rayonV, hauteur_lim)
plt.box(False)
plt.show()
fig.tight_layout()
fig.savefig(config.file_name)
##----------------------------FIN AFFICHAGE----------------------------------##
