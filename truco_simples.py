# -*- coding: utf-8 -*-
import random

#from interface_rodando import Screen

# Definindo cartas
class Carta:
    """ Carta do jogo de truco
    O valor vai de 0 a 9 representando as cartas 4, 5, ..., 3
    O naipe vai de 0 a 3 representando os naipes 
        ["Ouros", "Espada", "Copas", "Paus"] """
        
    valor_to_str = ["Quatro", "Cinco", "Seis", "Sete", "Dama",
                    "Valete", "Rei", "Ás", "Dois", "Três"]
    
    naipe_to_str = ["Ouros", "Espada", "Copas", "Paus"]
        
    def __init__(self, valor, naipe):
        self.valor = valor
        self.naipe = naipe
        
    def valor_str(self):
        return Carta.valor_to_str[self.valor]

    def naipe_str(self):
        return Carta.naipe_to_str[self.naipe]
        
    def valor_carta(self):
        return 4*self.valor + self.naipe
        
    def __str__(self):
        return self.valor_str() + " " + self.naipe_str()
 
def valor_to_carta(valor):
    valor_carta = valor // 4
    naipe_carta = valor % 4
    nova_carta = Carta(valor_carta, naipe_carta)
    return nova_carta

def compara_cartas(carta1, carta2):
    v1 = carta1.valor_carta()
    v2 = carta2.valor_carta()
    if v1 > v2:
        return 1
    else:
        return 2

class Baralho:
    def __init__(self):
        self.reinicia()
        
    def reinicia(self):
        self.baralho = list(range(40))
        
    def sortear_carta(self):
        k = random.randint(0, len(self.baralho) - 1)
        valor_carta = self.baralho[k]
        del self.baralho[k]
        return valor_carta
    
    def sortear_mao(self):
        mao = []
        for i in range(3):
            valor_carta = self.sortear_carta()
            carta = valor_to_carta(valor_carta)
            mao.append(carta)
        return mao
            
def jogada(jogador, mao):
    print("Cartas do jogador {0}".format(jogador))
    for carta in mao:
        print(carta, end=" ; ")
    print()
    c = int(input("Escolha sua carta: "))
    return c

class Jogo:
    def __init__(self):
        self.baralho = Baralho()
 
        self.resultado = 0 
 
        self.jogador = 1
        
        self.pontos_1 = 0
        self.pontos_2 = 0
        self.inicia_round()

    def recebe_jogada(self, indice_carta_na_mao):
        if self.jogador == 1:
            self.mesa_1 = self.mao_1[indice_carta_na_mao]
            self.mao_1[indice_carta_na_mao] = None
            self.jogador = 2
        else:
            self.mesa_2 = self.mao_2[indice_carta_na_mao]
            self.mao_2[indice_carta_na_mao] = None
            self.jogador = 1
            
        self.cartas_jogadas += 1
        
        if self.cartas_jogadas == 2:
            # Verifica quem ganhou esta mao.
            if compara_cartas(self.mesa_1, self.mesa_2) == 1:
                print("jogador 1 venceu esta mao")
                self.pontos_do_round_jogador_1 += 1
                self.jogador = 1
            else:
                print("jogador 2 venceu esta mao")
                self.pontos_do_round_jogador_2 += 1
                self.jogador = 2
                
            self.inicia_mao()
            
            # Verifica se o round acabou.
            if self.pontos_do_round_jogador_1 >= 2 or \
               self.pontos_do_round_jogador_2 >= 2:
                if self.pontos_do_round_jogador_1 > self.pontos_do_round_jogador_2:
                    print("Jogador 1 ganhou o round")
                    self.pontos_1 += 1
                    self.jogador = 1
                else:
                    print("Jogador 2 ganhou o round")
                    self.pontos_2 += 1
                    self.jogador = 2
                self.inicia_round()
                
                if self.pontos_1 == 12:
                    self.resultado = 1
                elif self.pontos_2 == 12:
                    self.resultado = 2                

    def inicia_mao(self):
        self.cartas_jogadas = 0
 
    def inicia_round(self):
        self.baralho.reinicia()

        self.mao_1 = self.baralho.sortear_mao()
        self.mao_2 = self.baralho.sortear_mao()

        self.pontos_do_round_jogador_1 = 0        
        self.pontos_do_round_jogador_2 = 0
        
        self.inicia_mao()
    
jogo = Jogo()

#while jogo.resultado == 0:
#    if jogo.jogador == 1:
#        c = jogada(1, jogo.mao_1)
#    else:
#        c = jogada(2, jogo.mao_2)
#    jogo.recebe_jogada(c)

print("Jogador {0} venceu!".format(jogo.resultado))
