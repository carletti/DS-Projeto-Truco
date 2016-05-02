# -*- coding: utf-8 -*-
import random as rdm

class cartas():
    
    def __init__(self):
        self.valor #= valor
        self.nype #= nype
        
   # def define_carta(self):
        

baralho = [['Quatro','Ouros'],
           ['Quatro', 'Espada'], 
           ['Quatro', 'Copas'],
           ['Quatro', 'Paus'],
           ['Cinco','Ouros'], 
           ['Cinco', 'Espada'],
           ['Cinco', 'Copas'], 
           ['Cinco', 'Paus'],
           ['Seis','Ouros'],
           ['Seis', 'Espada'], 
           ['Seis', 'Copas'],
           ['Seis', 'Paus'], 
           ['Sete','Ouros'],
           ['Sete', 'Espada'],
           ['Sete', 'Copas'],
           ['Sete', 'Paus'],
           ['Dama','Ouros'],
           ['Dama', 'Espada'],
           ['Dama', 'Copas'],
           ['Dama', 'Paus'], 
           ['Valete','Ouros'],
           ['Valete', 'Espada'],
           ['Valete', 'Copas'], 
           ['Valete', 'Paus'],
           ['Rei','Ouros'],
           ['Rei', 'Espada'],
           ['Rei', 'Copas'],
           ['Rei', 'Paus'],
           ['Ás','Ouros'],
           ['Ás', 'Espada'],
           ['Ás', 'Copas'],
           ['Ás', 'Paus'],
           ['Dois','Ouros'],
           ['Dois', 'Espada'], 
           ['Dois', 'Copas'],
           ['Dois', 'Paus'],
           ['Três','Ouros'],
           ['Três', 'Espada'], 
           ['Três', 'Copas'],
           ['Três', 'Paus']]
           
escolha = rdm.choice(baralho)
print (escolha)
print(baralho)
print(len(baralho))