# -*- coding: utf-8 -*-
"""
@author: José Manuel Alvarez - CI 25038805
"""
import os
import numpy as np
os.getcwd()
#------------------------------MODIFICAR-------------------------------------
os.chdir('/home/jose/Documentos/Tarea1_25038805/src')
#----------------------------------------------------------------------------
import pandas as pd
df = pd.read_csv("scraper/vista-minable.csv")
df.describe()

#Se transforman los tipos de datos iniciales para mejorar su tratamiento
df["marca"] = df["marca"].astype(str)
df["modelo"] = df["modelo"].astype(str)
df["precio"] = df["precio"].astype('float64')
df["precio_nuevo"] = df["precio_nuevo"].astype('float64')
df["precio_viejo"] = df["precio_viejo"].astype('float64')

#Debido a que el precio se presenta algunas veces como Precio nuevo contra Precio viejo (rebaja)
#o como precio solo, se deben replicar los valores necesarios para que al procesar el dataset no
#se encuentren valores NaN
nullPrices = np.isnan(df["precio"]) 
nullOldPrices = np.isnan(df["precio_viejo"]) 
nullNewPrices = np.isnan(df["precio_nuevo"]) 
tam = df["marca"].size

for x in range(0,tam):
    if nullPrices[x] == True:
        df["precio"][x] = df["precio_nuevo"][x]
    else:
         df["precio_nuevo"][x] = df["precio"][x]
         df["precio_viejo"][x] = df["precio"][x]
        