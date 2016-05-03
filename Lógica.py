# -*- coding: utf-8 -*-
import random
# Definindo cartas

class cartas:
    
    def __init__(self, valor, nype):
        self.valor = valor
        self. nype = nype
        
class baralho:
    
    def __init__(self):
        self.nome_cartas =  ['Quatro Ouros',
                             'Quatro Espada', 
                             'Quatro Copas',
                             'Quatro Paus',
                             'Cinco Ouros', 
                             'Cinco Espada',
                             'Cinco Copas', 
                             'Cinco Paus',
                             'Seis Ouros',
                             'Seis Espada', 
                             'Seis Copas',
                             'Seis Paus', 
                             'Sete Ouros',
                             'Sete Espada',
                             'Sete Copas',
                             'Sete Paus',
                             'Dama Ouros',
                             'Dama Espada',
                             'Dama Copas',
                             'Dama Paus', 
                             'Valete Ouros',
                             'Valete Espada',
                             'Valete Copas', 
                             'Valete Paus',
                             'Rei Ouros',
                             'Rei Espada',
                             'Rei Copas',
                             'Rei Paus',
                             'Ás Ouros',
                             'Ás Espada',
                             'Ás Copas',
                             'Ás Paus',
                             'Dois Ouros',
                             'Dois Espada', 
                             'Dois Copas',
                             'Dois Paus',
                             'Três Ouros',
                             'Três Espada', 
                             'Três Copas',
                             'Três Paus']
        self.cartas = [x for x in range (40)]
        
    def reiniciar(self):
        self.cartas = self.cartas
        return self.cartas
        
    def comprar_carta(self):
        i = random.randint(0, len(self.cartas)-1)
        carta = self.cartas[i]
        del self.cartas[i]
        return carta
        
    def sortear(self):
        sorteio = {1:[self.comprar_carta(),
                      self.comprar_carta(),
                      self.comprar_carta()],
                   2:[self.comprar_carta(),
                      self.comprar_carta(),
                      self.comprar_carta()],
                   3:[self.comprar_carta(),
                      self.comprar_carta(),
                      self.comprar_carta()],
                   4:[self.comprar_carta(),
                      self.comprar_carta(),
                      self.comprar_carta()],
                   "Manilha":self.comprar_carta()}
        self.reiniciar()
        return sorteio
    
# Teste        
baralho_de_truco = baralho()
s = baralho_de_truco.sortear()
print (s)
c = baralho_de_truco.reiniciar()
print (c)
            