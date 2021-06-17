#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 08:09:28 2021

@author: yvan
"""
largeur_lim = 21e-2 #largeur horizontal image (m)
hauteur_lim = 29.7e-2 #hauteur horizontal image (m)
rayonH = 1e-3 #rayon horizontal (m)
rayonV = 3e-3 #rayon vertical (m)
ecartH = 2e-3 #ecart entre deux ellipses (m)
file_name = "/Users/yvan/Desktop/ETS_montreal/Cours/E21/MTR892/Speckle_LI_H_"+str(int(rayonH*1000))+"_V_"+str(int(rayonV*1000))+"_E_"+str(int(ecartH*1000))+".pdf" # Nom chemin sauvegarde fichier