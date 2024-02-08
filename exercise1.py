#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 22:41:33 2024

@author: hpord
"""

import os 
os.chdir("/home/hpord/Documentos/grupodiscord/Programming-Skills-Level2")
#%%
from random import randint
    
#%%
class Generador_Fixture:
    def __init__(self, equipos):
        self._equipos = equipos
        self._map_partidos = {}
        self.generar_partidos()
    
    def generar_partidos(self):
        for equipo in self._equipos:
            map_partido_result = {}
            for rival in self._equipos:
                if equipo == rival: continue
                map_partido_result[rival] = []
            self._map_partidos[equipo] = map_partido_result
            
    def mostrar_partidos(self):
        for partido in self._map_partidos:
            print(partido, self._map_partidos[partido])
            
    @property
    def map_partidos(self):
        return self._map_partidos
    #@map_partidos.setter
    def agregar_resultado(self, equipo, rival, resultado):
        self._map_partidos[equipo][rival].append((resultado[0], resultado[1]))
        self._map_partidos[rival][equipo].append((resultado[1], resultado[0]))

#%%
class Generador_Resultados:
    def __init__(self, partidos):
        pass
    
#%%
def generar_resultados(partidos, equipos):
    for i in range(len(equipos)-1):
        for j in range(i+1, len(equipos)):
            for k in range(3):
                partidos.agregar_resultado(equipos[i], equipos[j], (randint(0, 9), randint(0, 9)))

#%%
def generar_tabla(partidos, equipos):
    tabla = {}
    for equipo in equipos:
        tabla[equipo] = [0, 0, 0]
        for rival in partidos.map_partidos[equipo]:
            pass

#%%
def main():
    big_six = [
        'Manchester United',
        'Liverpool',
        'Arsenal',
        'Chelsea',
        'Manchester City',
        'Tottenham Hotspur'
        ]
    partidos = Generador_Fixture(big_six)
    generar_resultados(partidos, big_six)
    partidos.mostrar_partidos()
    print()
    generar_tabla(partidos, big_six)
    

#%%
if __name__ == '__main__':
    main()