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
        self.cartas_em_jogo = []
        for a in self.cartas:
            self.cartas_em_jogo.append(a)
        self.nome_cartas_em_jogo = []
        for b in self.nome_cartas:
            self.nome_cartas_em_jogo.append(b)
        
    def reiniciar_cartas_em_jogo(self):
        self.cartas_em_jogo = self.cartas
        return self.cartas_em_jogo
        
    def reiniciar_nome_cartas_em_jogo(self):
        self.nome_cartas_em_jogo = self.nome_cartas
        return self.nome_cartas_em_jogo
        
    def comprar_carta(self):
        i = random.randint(0, len(self.cartas_em_jogo)-1)
        print (i)
        print (self.cartas_em_jogo[i])
        print (self.nome_cartas_em_jogo[i])
        numero_carta = self.cartas_em_jogo[i]
        carta = self.nome_cartas_em_jogo[i]
        self.cartas_em_jogo.remove(numero_carta)
        self.nome_cartas_em_jogo.remove(carta)
        return carta
       
    def sortear(self):
        self.sorteio = {1:[self.comprar_carta(),
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
                    "Vira":self.comprar_carta()}
        self.reiniciar_cartas_em_jogo()
        self.reiniciar_nome_cartas_em_jogo()
        return self.sorteio
    
# Teste        
baralho_de_truco = baralho()
s = baralho_de_truco.sortear()
print (s)
c = baralho_de_truco.reiniciar_nome_cartas_em_jogo()
print (c)
d = baralho_de_truco.reiniciar_cartas_em_jogo()
print (d)

class jogador:

    def __init__(self, número, cartas):
        self.número = número
        self.cartas = cartas
        
    def define_jogador(self):
        for i, j in self.sorteio:
            return 'O jogador {0} tem as cartas {1}'.format(i, j)
            
jogadores_de_truco = jogador
a = jogadores_de_truco.define_jogador()
print (a)
                   