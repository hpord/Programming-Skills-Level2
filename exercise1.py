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
    
    def agregar_resultado(self, equipo, rival, resultado):
        self._map_partidos[equipo][rival].append([resultado[0], resultado[1]])
        self._map_partidos[rival][equipo].append([resultado[1], resultado[0]])

    
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
        tabla[equipo] = [0, 0, 0, 0, 0, 0, 0, 0]
        
        for rival in partidos.map_partidos[equipo]:
            tabla[equipo][0] += 3
            for k in range(3):
                goles_equipo = partidos.map_partidos[equipo][rival][k][0]
                goles_rival = partidos.map_partidos[equipo][rival][k][1]
                #print(goles_equipo, tabla[equipo][0])
                tabla[equipo][4] += goles_equipo
                tabla[equipo][5] += goles_rival
                tabla[equipo][6] = tabla[equipo][4] - tabla[equipo][5]
                if goles_equipo > goles_rival:
                    tabla[equipo][1] += 1
                    tabla[equipo][7] += 3
                elif goles_equipo == goles_rival:
                    tabla[equipo][2] += 1
                    tabla[equipo][7] += 1
                else: tabla[equipo][3] += 1
    
    tabla_ord = [[equipo, *tabla[equipo]] for equipo in tabla]
    ordenar(tabla_ord)
    print(f"EQUIPO                 PJ   PG   PE   PP   GF   GC   DG   Ptos")
    for team in tabla_ord:
        print(f"{team[0]:20} {team[1]:4d} {team[2]:4d} {team[3]:4d} {team[4]:4d} {team[5]:4d} {team[6]:4d} {team[7]:4d} {team[8]:6d}")
            
#%%
def ordenar(tabla_lista):
    for i in range(len(tabla_lista)-1):
        for j in range(i+1, len(tabla_lista)):
            if tabla_lista[j][8] > tabla_lista[i][8]:
                tabla_lista[i], tabla_lista[j] = tabla_lista[j], tabla_lista[i]
            elif tabla_lista[j][8] == tabla_lista[i][8]:
                if tabla_lista[j][7] > tabla_lista[i][7]:
                    tabla_lista[i], tabla_lista[j] = tabla_lista[j], tabla_lista[i]
                elif tabla_lista[j][7] == tabla_lista[i][7]:
                    if tabla_lista[j][5] == tabla_lista[i][5]:
                        tabla_lista[i], tabla_lista[j] = tabla_lista[j], tabla_lista[i]
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
    print()
    generar_tabla(partidos, big_six)
    

#%%
if __name__ == '__main__':
    main()