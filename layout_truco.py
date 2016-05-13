# -*- coding: utf-8 -*-
import tkinter as tk
import random

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
                
                if self.pontos_1 == 3:
                    self.resultado = 1
                elif self.pontos_2 == 3:
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

class Screen:
    def __init__(self):
        self.screen = tk.Tk()        
        self.screen.title('Truco')
        self.screen.geometry('650x600+300+50')
        self.screen.configure(bg = "green")
        
        #Construindo as Linhas
        self.screen.rowconfigure(0, minsize = 10, weight = 1)
        self.screen.rowconfigure(1, minsize = 200, weight = 1)
        self.screen.rowconfigure(2, minsize = 15, weight = 1)
        self.screen.rowconfigure(3, minsize = 200, weight = 1)
        self.screen.rowconfigure(4, minsize = 15, weight = 1)
        self.screen.rowconfigure(5, minsize = 200, weight = 1)
        self.screen.rowconfigure(6, minsize = 10, weight = 1)

        #Construindo as colunas
        self.screen.columnconfigure(0, minsize = 10, weight = 1)
        self.screen.columnconfigure(1, minsize = 100, weight = 1)
        self.screen.columnconfigure(2, minsize = 10, weight = 1)
        self.screen.columnconfigure(3, minsize = 100, weight = 1)
        self.screen.columnconfigure(4, minsize = 10, weight = 1)
        self.screen.columnconfigure(5, minsize = 100, weight = 1)
        self.screen.columnconfigure(6, minsize = 10, weight = 1)
        self.screen.columnconfigure(7, minsize = 100, weight = 1)
        self.screen.columnconfigure(8, minsize = 10, weight = 1)
        self.screen.columnconfigure(9, minsize = 100, weight = 1)
        self.screen.columnconfigure(10, minsize = 10, weight = 1)

        #Cartas
        self.carta_1_jogador_1 = tk.Button(self.screen)
        self.carta_1_jogador_1.configure(text = 'Carta 1', bg = 'white', command= self.carta_1_jogador_1_clicada)
        self.carta_1_jogador_1.grid(row = 1, column = 1, sticky= "nsew")
        
        self.carta_2_jogador_1 = tk.Button(self.screen)
        self.carta_2_jogador_1.configure(bg = 'white', text = 'Carta 2', command= self.carta_2_jogador_1_clicada)
        self.carta_2_jogador_1.grid(row = 1, column = 3, sticky= "nsew")
        
        self.carta_3_jogador_1 = tk.Button(self.screen)
        self.carta_3_jogador_1.configure(bg = 'white', text = 'Carta 3', command= self.carta_3_jogador_1_clicada)
        self.carta_3_jogador_1.grid(row = 1, column = 5, sticky= "nsew")
        
        #Botão para pedir TRUCO!
     #   truco = tk.Button(self.screen)
     #   truco.configure(text = 'TRUCO !')
     #   truco.configure(width = 15, height = 5)
     #   truco.configure(bg = 'red')
     #   truco.grid(row = 2, column = 0)

        #Displays - em canvas
        self.carta_1_jogador_2 = tk.Button(self.screen)
        self.carta_1_jogador_2.grid(row = 5, column = 5, sticky= "nsew")
        self.carta_1_jogador_2.configure(bg = 'yellow', command= self.carta_1_jogador_2_clicada)
        
        self.carta_2_jogador_2 = tk.Button(self.screen)
        self.carta_2_jogador_2.grid(row = 5, column = 7, sticky= "nsew")
        self.carta_2_jogador_2.configure(bg = 'yellow', command= self.carta_2_jogador_2_clicada)
        
        self.carta_3_jogador_2 = tk.Button(self.screen)
        self.carta_3_jogador_2.grid(row = 5, column = 9, sticky= "nsew")
        self.carta_3_jogador_2.configure(bg = 'yellow', command= self.carta_3_jogador_2_clicada)

        self.jogador_2 = tk.Label(self.screen)
        self.jogador_2.grid(row= 5, column= 3, sticky= "nsew")
        self.jogador_2.configure(bg= "green", text= "Jogador 2", font= "arial 15 bold")

        self.jogador_1 = tk.Label(self.screen)
        self.jogador_1.grid(row= 1, column= 7, sticky= "nsew")
        self.jogador_1.configure(bg= "green", text= "Jogador 1", font= "arial 15 bold")

        self.carta_jogada_jogador_1 = tk.Label()
        self.carta_jogada_jogador_1.configure(bg= "light grey")
        self.carta_jogada_jogador_1.grid(row= 3, column= 3, sticky= "nsew")

        self.carta_jogada_jogador_2 = tk.Label()
        self.carta_jogada_jogador_2.configure(bg= "light grey")
        self.carta_jogada_jogador_2.grid(column= 7, row= 3, sticky= "nsew")

        versus= tk.Label()
        versus.configure(text= "X", font= "arial 56 bold", bg= "green")
        versus.grid(row= 3, column= 5, sticky= "nsew")
    
    def carta_1_jogador_1_clicada(self):
        self.carta_1_jogador_1.configure(bg="green", state= "disabled", bd= 0, text= "")

    def carta_2_jogador_1_clicada(self):
        self.carta_2_jogador_1.configure(bg="green", state= "disabled", bd= 0, text= "")

    def carta_3_jogador_1_clicada(self):
        self.carta_3_jogador_1.configure(bg="green", state= "disabled", bd= 0, text= "")

    def carta_1_jogador_2_clicada(self):
        self.carta_1_jogador_2.configure(bg="green", state= "disabled", bd= 0, text= "")

    def carta_2_jogador_2_clicada(self):
        self.carta_2_jogador_2.configure(bg="green", state= "disabled", bd= 0, text= "")    

    def carta_3_jogador_2_clicada(self):
        self.carta_3_jogador_2.configure(bg="green", state= "disabled", bd= 0, text= "")

    def start(self):
        self.screen.mainloop()

jogo = Jogo()
app = Screen()
app.start()

#Sincronizando o Layout com a lógica do jogo
    

while jogo.resultado == 0:
    if jogo.jogador == 1:
        c = jogada(1, jogo.mao_1)
    else:
        c = jogada(2, jogo.mao_2)
    jogo.recebe_jogada(c)

print("Jogador {0} venceu!".format(jogo.resultado))