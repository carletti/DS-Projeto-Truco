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
        self.screen.columnconfigure(1, minsize = 125, weight = 1)
        self.screen.columnconfigure(2, minsize = 10, weight = 1)
        self.screen.columnconfigure(3, minsize = 125, weight = 1)
        self.screen.columnconfigure(4, minsize = 10, weight = 1)
        self.screen.columnconfigure(5, minsize = 125, weight = 1)
        self.screen.columnconfigure(6, minsize = 10, weight = 1)
        self.screen.columnconfigure(7, minsize = 125, weight = 1)
        self.screen.columnconfigure(8, minsize = 10, weight = 1)
        self.screen.columnconfigure(9, minsize = 125, weight = 1)
        self.screen.columnconfigure(10, minsize = 10, weight = 1)

        #Adicionando as imagens das cartas

        self.As_Ouros=tk.PhotoImage(file= "A_pica.png")
        self.As_Espadas=tk.PhotoImage(file= "A_espadas.png")
        self.As_Copas=tk.PhotoImage(file= "A_copas.png")
        self.As_Paus=tk.PhotoImage(file= "A_zap.png")
        self.Dois_Ouros=tk.PhotoImage(file= "2_pica.png")
        self.Dois_Espadas=tk.PhotoImage(file= "2_espadas.png")
        self.Dois_Copas=tk.PhotoImage(file= "2_copas.png")
        self.Dois_Paus=tk.PhotoImage(file= "2_zap.png")
        self.Tres_Ouros=tk.PhotoImage(file= "3_pica.png")
        self.Tres_Espadas=tk.PhotoImage(file= "3_espadas.png")
        self.Tres_Copas=tk.PhotoImage(file= "3_copas.png")
        self.Tres_Paus=tk.PhotoImage(file= "3_zap.png")
        self.Quatro_Ouros=tk.PhotoImage(file= "4_pica.png")
        self.Quatro_Espadas=tk.PhotoImage(file= "4_espadas.png")
        self.Quatro_Copas=tk.PhotoImage(file= "4_copas.png")
        self.Quatro_Paus=tk.PhotoImage(file= "4_zap.png")
        self.Cinco_Ouros=tk.PhotoImage(file= "5_pica.png")
        self.Cinco_Espadas=tk.PhotoImage(file= "5_espadas.png")
        self.Cinco_Copas=tk.PhotoImage(file= "5_copas.png")
        self.Cinco_Paus=tk.PhotoImage(file= "5_zap.png")
        self.Seis_Ouros=tk.PhotoImage(file= "6_pica.png")
        self.Seis_Espadas=tk.PhotoImage(file= "6_espadas.png")
        self.Seis_Copas=tk.PhotoImage(file= "6_copas.png")
        self.Seis_Paus=tk.PhotoImage(file= "6_zap.png")
        self.Sete_Ouros=tk.PhotoImage(file= "7_pica.png")
        self.Sete_Espadas=tk.PhotoImage(file= "7_espadas.png")
        self.Sete_Copas=tk.PhotoImage(file= "7_copas.png")
        self.Sete_Paus=tk.PhotoImage(file= "7_zap.png")
        self.Dama_Ouros=tk.PhotoImage(file= "Q_pica.png")
        self.Dama_Espadas=tk.PhotoImage(file= "Q_espadas.png")
        self.Dama_Copas=tk.PhotoImage(file= "Q_copas.png")
        self.Dama_Paus=tk.PhotoImage(file= "Q_zap.png")
        self.Valete_Ouros=tk.PhotoImage(file= "J_pica.png")
        self.Valete_Espadas=tk.PhotoImage(file= "J_espadas.png")
        self.Valete_Copas=tk.PhotoImage(file= "J_copas.png")
        self.Valete_Paus=tk.PhotoImage(file= "J_zap.png")
        self.Rei_Ouros=tk.PhotoImage(file= "K_pica.png")
        self.Rei_Espadas=tk.PhotoImage(file= "K_espadas.png")
        self.Rei_Copas=tk.PhotoImage(file= "K_copa.png")
        self.Rei_Copas=tk.PhotoImage(file= "K_copa.png")
        self.Rei_Paus=tk.PhotoImage(file= "K_zap.png")

        #Cartas
        self.carta_1_jogador_1 = tk.Button(self.screen)
        self.carta_1_jogador_1.configure(text = 'Carta 1', bg = 'green', command= self.carta_1_jogador_1_clicada, image= self.Dama_Ouros, bd= 0)
        self.carta_1_jogador_1.grid(row = 1, column = 1, sticky= "nsew")
        
        self.carta_2_jogador_1 = tk.Button(self.screen)
        self.carta_2_jogador_1.configure(bg = 'white', text = 'Carta 2', command= self.carta_2_jogador_1_clicada)
        self.carta_2_jogador_1.grid(row = 1, column = 3, sticky= "nsew")
        
        self.carta_3_jogador_1 = tk.Button(self.screen)
        self.carta_3_jogador_1.configure(bg = 'white', text = 'Carta 3', command= self.carta_3_jogador_1_clicada)
        self.carta_3_jogador_1.grid(row = 1, column = 5, sticky= "nsew")

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
    
        

    #Criando os Callbacks dos botões

    def carta_1_jogador_1_clicada(self):
        self.carta_1_jogador_1.configure(bg="green", state= "disabled", bd= 0, text= "", image= None)

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

    #Colocando a primeira carta do jogador 1 no layout
if jogo.mao_1[0] == "Ás Ouros":
    screen.carta_1_jogador_1.configure(image=self.As_Ouros)
elif jogo.mao_1[0] == "Ás Espadas":
    screen.carta_1_jogador_1.configure(image= self.As_Espadas)
elif jogo.mao_1[0] == "Ás Copas":
    screen.carta_1_jogador_1.configure(image= self.As_Copas)
elif jogo.mao_1[0] == "Ás Paus":
    screen.carta_1_jogador_1.configure(image= self.As_Paus)
elif jogo.mao_1[0] == "Dois Ouros":
    screen.carta_1_jogador_1.configure(image= self.Dois_Ouros)
elif jogo.mao_1[0] == "Dois Ouros":
    screen.carta_1_jogador_1.configure(image= self.Dois_Espadas)
elif jogo.mao_1[0] == "Dois Espadas":
    screen.carta_1_jogador_1.configure(image= self.Dois_Copas)
elif jogo.mao_1[0] == "Dois Paus":
    screen.carta_1_jogador_1.configure(image= self.Dois_Paus)
elif jogo.mao_1[0] == "Tres Ouros":
    screen.carta_1_jogador_1.configure(image= self.Tres_Ouros)
elif jogo.mao_1[0] == "Tres Espadas":
    screen.carta_1_jogador_1.configure(image= self.Tres_Espadas)
elif jogo.mao_1[0] == "Tres Copas":
    screen.carta_1_jogador_1.configure(image= self.Tres_Copas)
elif jogo.mao_1[0] == "Tres Paus":
    screen.carta_1_jogador_1.configure(image= self.Tres_Paus)
elif jogo.mao_1[0] == "Quatro Ouros":
    screen.carta_1_jogador_1.configure(image= self.Quatro_Ouros)
elif jogo.mao_1[0] == "Quatro Espadas":
    screen.carta_1_jogador_1.configure(image= self.Quatro_Espadas)
elif jogo.mao_1[0] == "Quatro Copas":
    screen.carta_1_jogador_1.configure(image= self.Quatro_Copas)
elif jogo.mao_1[0] == "Quatro Paus":
    screen.carta_1_jogador_1.configure(image= self.Quatro_Paus)
elif jogo.mao_1[0] == "Cinco Ouros":
    screen.carta_1_jogador_1.configure(image= self.Cinco_Ouros)
elif jogo.mao_1[0] == "Cinco Espadas":
    screen.carta_1_jogador_1.configure(image= self.Cinco_Espadas)
elif jogo.mao_1[0] == "Cinco Copas":
    screen.carta_1_jogador_1.configure(image= self.Cinco_Copas)
elif jogo.mao_1[0] == "Cinco Paus":
    screen.carta_1_jogador_1.configure(image= self.Cinco_Paus)
elif jogo.mao_1[0] == "Seis Ouros":
    screen.carta_1_jogador_1.configure(image= self.Seis_Ouros)
elif jogo.mao_1[0] == "Seis Espadas":
    screen.carta_1_jogador_1.configure(image= self.Seis_Espadas)
elif jogo.mao_1[0] == "Seis Copas":
    screen.carta_1_jogador_1.configure(image= self.Seis_Copas)
elif jogo.mao_1[0] == "Seis Paus":
    screen.carta_1_jogador_1.configure(image= self.Seis_Paus)
elif jogo.mao_1[0] == "Sete Ouros":
    screen.carta_1_jogador_1.configure(image= self.Sete_Ouros)
elif jogo.mao_1[0] == "Sete Espadas":
    screen.carta_1_jogador_1.configure(image= self.Sete_Espadas)
elif jogo.mao_1[0] == "Sete Copas":
    screen.carta_1_jogador_1.configure(image= self.Sete_Copas)
elif jogo.mao_1[0] == "Sete Paus":
    screen.carta_1_jogador_1.configure(image= self.Sete_Paus)
elif jogo.mao_1[0] == "Dama Ouros":
    screen.carta_1_jogador_1.configure(image= self.Dama_Ouros)
elif jogo.mao_1[0] == "Dama Espadas":
    screen.carta_1_jogador_1.configure(image= self.Dama_Espadas)
elif jogo.mao_1[0] == "Dama Copas":
    screen.carta_1_jogador_1.configure(image= self.Dama_Copas)
elif jogo.mao_1[0] == "Dama Paus":
    screen.carta_1_jogador_1.configure(image= self.Dama_Paus)
elif jogo.mao_1[0] == "Valete Ouros":
    screen.carta_1_jogador_1.configure(image= self.Valete_Ouros)
elif jogo.mao_1[0] == "Valete Espadas":
    screen.carta_1_jogador_1.configure(image= self.Valete_Espadas)
elif jogo.mao_1[0] == "Valete Copas":
    screen.carta_1_jogador_1.configure(image= self.Valete_Copas)
elif jogo.mao_1[0] == "Valete Paus":
    screen.carta_1_jogador_1.configure(image= self.Valete_Paus)
elif jogo.mao_1[0] == "Rei Ouros":
    screen.carta_1_jogador_1.configure(image= self.Rei_Ouros)
elif jogo.mao_1[0] == "Rei Espadas":
    screen.carta_1_jogador_1.configure(image= self.Rei_Espadas)
elif jogo.mao_1[0] == "Rei Copas":
    screen.carta_1_jogador_1.configure(image= self.Rei_Copas)
elif jogo.mao_1[0] == "Rei Paus":
    screen.carta_1_jogador_1.configure(image= self.Rei_Paus)

    #Colocando a segunda carta do jogador 1 no Layout
if jogo.mao_1[1] == "Ás Ouros":
    screen.carta_1_jogador_1.configure(image=self.As_Ouros)
elif jogo.mao_1[1] == "Ás Espadas":
    screen.carta_1_jogador_1.configure(image= self.As_Espadas)
elif jogo.mao_1[1] == "Ás Copas":
    screen.carta_1_jogador_1.configure(image= self.As_Copas)
elif jogo.mao_1[1] == "Ás Paus":
    screen.carta_1_jogador_1.configure(image= self.As_Paus)
elif jogo.mao_1[1] == "Dois Ouros":
    screen.carta_1_jogador_1.configure(image= self.Dois_Ouros)
elif jogo.mao_1[1] == "Dois Ouros":
    screen.carta_1_jogador_1.configure(image= self.Dois_Espadas)
elif jogo.mao_1[1] == "Dois Espadas":
    screen.carta_1_jogador_1.configure(image= self.Dois_Copas)
elif jogo.mao_1[1] == "Dois Paus":
    screen.carta_1_jogador_1.configure(image= self.Dois_Paus)
elif jogo.mao_1[1] == "Tres Ouros":
    screen.carta_1_jogador_1.configure(image= self.Tres_Ouros)
elif jogo.mao_1[1] == "Tres Espadas":
    screen.carta_1_jogador_1.configure(image= self.Tres_Espadas)
elif jogo.mao_1[1] == "Tres Copas":
    screen.carta_1_jogador_1.configure(image= self.Tres_Copas)
elif jogo.mao_1[1] == "Tres Paus":
    screen.carta_1_jogador_1.configure(image= self.Tres_Paus)
elif jogo.mao_1[1] == "Quatro Ouros":
    screen.carta_1_jogador_1.configure(image= self.Quatro_Ouros)
elif jogo.mao_1[1] == "Quatro Espadas":
    screen.carta_1_jogador_1.configure(image= self.Quatro_Espadas)
elif jogo.mao_1[1] == "Quatro Copas":
    screen.carta_1_jogador_1.configure(image= self.Quatro_Copas)
elif jogo.mao_1[1] == "Quatro Paus":
    screen.carta_1_jogador_1.configure(image= self.Quatro_Paus)
elif jogo.mao_1[1] == "Cinco Ouros":
    screen.carta_1_jogador_1.configure(image= self.Cinco_Ouros)
elif jogo.mao_1[1] == "Cinco Espadas":
    screen.carta_1_jogador_1.configure(image= self.Cinco_Espadas)
elif jogo.mao_1[1] == "Cinco Copas":
    screen.carta_1_jogador_1.configure(image= self.Cinco_Copas)
elif jogo.mao_1[1] == "Cinco Paus":
    screen.carta_1_jogador_1.configure(image= self.Cinco_Paus)
elif jogo.mao_1[1] == "Seis Ouros":
    screen.carta_1_jogador_1.configure(image= self.Seis_Ouros)
elif jogo.mao_1[1] == "Seis Espadas":
    screen.carta_1_jogador_1.configure(image= self.Seis_Espadas)
elif jogo.mao_1[1] == "Seis Copas":
    screen.carta_1_jogador_1.configure(image= self.Seis_Copas)
elif jogo.mao_1[1] == "Seis Paus":
    screen.carta_1_jogador_1.configure(image= self.Seis_Paus)
elif jogo.mao_1[1] == "Sete Ouros":
    screen.carta_1_jogador_1.configure(image= self.Sete_Ouros)
elif jogo.mao_1[1] == "Sete Espadas":
    screen.carta_1_jogador_1.configure(image= self.Sete_Espadas)
elif jogo.mao_1[1] == "Sete Copas":
    screen.carta_1_jogador_1.configure(image= self.Sete_Copas)
elif jogo.mao_1[1] == "Sete Paus":
    screen.carta_1_jogador_1.configure(image= self.Sete_Paus)
elif jogo.mao_1[1] == "Dama Ouros":
    screen.carta_1_jogador_1.configure(image= self.Dama_Ouros)
elif jogo.mao_1[1] == "Dama Espadas":
    screen.carta_1_jogador_1.configure(image= self.Dama_Espadas)
elif jogo.mao_1[1] == "Dama Copas":
    screen.carta_1_jogador_1.configure(image= self.Dama_Copas)
elif jogo.mao_1[1] == "Dama Paus":
    screen.carta_1_jogador_1.configure(image= self.Dama_Paus)
elif jogo.mao_1[1] == "Valete Ouros":
    screen.carta_1_jogador_1.configure(image= self.Valete_Ouros)
elif jogo.mao_1[1] == "Valete Espadas":
    screen.carta_1_jogador_1.configure(image= self.Valete_Espadas)
elif jogo.mao_1[1] == "Valete Copas":
    screen.carta_1_jogador_1.configure(image= self.Valete_Copas)
elif jogo.mao_1[1] == "Valete Paus":
    screen.carta_1_jogador_1.configure(image= self.Valete_Paus)
elif jogo.mao_1[1] == "Rei Ouros":
    screen.carta_1_jogador_1.configure(image= self.Rei_Ouros)
elif jogo.mao_1[1] == "Rei Espadas":
    screen.carta_1_jogador_1.configure(image= self.Rei_Espadas)
elif jogo.mao_1[1] == "Rei Copas":
    screen.carta_1_jogador_1.configure(image= self.Rei_Copas)
elif jogo.mao_1[1] == "Rei Paus":
    screen.carta_1_jogador_1.configure(image= self.Rei_Paus)

    #Colocando a terceira carta do jogador 1 no Layout

if jogo.mao_1[2] == "Ás Ouros":
    screen.carta_1_jogador_1.configure(image=self.As_Ouros)
elif jogo.mao_1[2] == "Ás Espadas":
    screen.carta_1_jogador_1.configure(image= self.As_Espadas)
elif jogo.mao_1[2] == "Ás Copas":
    screen.carta_1_jogador_1.configure(image= self.As_Copas)
elif jogo.mao_1[2] == "Ás Paus":
    screen.carta_1_jogador_1.configure(image= self.As_Paus)
elif jogo.mao_1[2] == "Dois Ouros":
    screen.carta_1_jogador_1.configure(image= self.Dois_Ouros)
elif jogo.mao_1[2] == "Dois Ouros":
    screen.carta_1_jogador_1.configure(image= self.Dois_Espadas)
elif jogo.mao_1[2] == "Dois Espadas":
    screen.carta_1_jogador_1.configure(image= self.Dois_Copas)
elif jogo.mao_1[2] == "Dois Paus":
    screen.carta_1_jogador_1.configure(image= self.Dois_Paus)
elif jogo.mao_1[2] == "Tres Ouros":
    screen.carta_1_jogador_1.configure(image= self.Tres_Ouros)
elif jogo.mao_1[2] == "Tres Espadas":
    screen.carta_1_jogador_1.configure(image= self.Tres_Espadas)
elif jogo.mao_1[2] == "Tres Copas":
    screen.carta_1_jogador_1.configure(image= self.Tres_Copas)
elif jogo.mao_1[2] == "Tres Paus":
    screen.carta_1_jogador_1.configure(image= self.Tres_Paus)
elif jogo.mao_1[2] == "Quatro Ouros":
    screen.carta_1_jogador_1.configure(image= self.Quatro_Ouros)
elif jogo.mao_1[2] == "Quatro Espadas":
    screen.carta_1_jogador_1.configure(image= self.Quatro_Espadas)
elif jogo.mao_1[2] == "Quatro Copas":
    screen.carta_1_jogador_1.configure(image= self.Quatro_Copas)
elif jogo.mao_1[2] == "Quatro Paus":
    screen.carta_1_jogador_1.configure(image= self.Quatro_Paus)
elif jogo.mao_1[2] == "Cinco Ouros":
    screen.carta_1_jogador_1.configure(image= self.Cinco_Ouros)
elif jogo.mao_1[2] == "Cinco Espadas":
    screen.carta_1_jogador_1.configure(image= self.Cinco_Espadas)
elif jogo.mao_1[2] == "Cinco Copas":
    screen.carta_1_jogador_1.configure(image= self.Cinco_Copas)
elif jogo.mao_1[2] == "Cinco Paus":
    screen.carta_1_jogador_1.configure(image= self.Cinco_Paus)
elif jogo.mao_1[2] == "Seis Ouros":
    screen.carta_1_jogador_1.configure(image= self.Seis_Ouros)
elif jogo.mao_1[2] == "Seis Espadas":
    screen.carta_1_jogador_1.configure(image= self.Seis_Espadas)
elif jogo.mao_1[2] == "Seis Copas":
    screen.carta_1_jogador_1.configure(image= self.Seis_Copas)
elif jogo.mao_1[2] == "Seis Paus":
    screen.carta_1_jogador_1.configure(image= self.Seis_Paus)
elif jogo.mao_1[2] == "Sete Ouros":
    screen.carta_1_jogador_1.configure(image= self.Sete_Ouros)
elif jogo.mao_1[2] == "Sete Espadas":
    screen.carta_1_jogador_1.configure(image= self.Sete_Espadas)
elif jogo.mao_1[2] == "Sete Copas":
    screen.carta_1_jogador_1.configure(image= self.Sete_Copas)
elif jogo.mao_1[2] == "Sete Paus":
    screen.carta_1_jogador_1.configure(image= self.Sete_Paus)
elif jogo.mao_1[2] == "Dama Ouros":
    screen.carta_1_jogador_1.configure(image= self.Dama_Ouros)
elif jogo.mao_1[2] == "Dama Espadas":
    screen.carta_1_jogador_1.configure(image= self.Dama_Espadas)
elif jogo.mao_1[2] == "Dama Copas":
    screen.carta_1_jogador_1.configure(image= self.Dama_Copas)
elif jogo.mao_1[2] == "Dama Paus":
    screen.carta_1_jogador_1.configure(image= self.Dama_Paus)
elif jogo.mao_1[2] == "Valete Ouros":
    screen.carta_1_jogador_1.configure(image= self.Valete_Ouros)
elif jogo.mao_1[2] == "Valete Espadas":
    screen.carta_1_jogador_1.configure(image= self.Valete_Espadas)
elif jogo.mao_1[2] == "Valete Copas":
    screen.carta_1_jogador_1.configure(image= self.Valete_Copas)
elif jogo.mao_1[2] == "Valete Paus":
    screen.carta_1_jogador_1.configure(image= self.Valete_Paus)
elif jogo.mao_1[2] == "Rei Ouros":
    screen.carta_1_jogador_1.configure(image= self.Rei_Ouros)
elif jogo.mao_1[2] == "Rei Espadas":
    screen.carta_1_jogador_1.configure(image= self.Rei_Espadas)
elif jogo.mao_1[2] == "Rei Copas":
    screen.carta_1_jogador_1.configure(image= self.Rei_Copas)
elif jogo.mao_1[2] == "Rei Paus":
    screen.carta_1_jogador_1.configure(image= self.Rei_Paus)

    #Colocando a primeira carta do jogador 2 no Layout
if jogo.mao_2[0] == "Ás Ouros":
    screen.carta_1_jogador_1.configure(image=self.As_Ouros)
elif jogo.mao_2[0] == "Ás Espadas":
    screen.carta_1_jogador_1.configure(image= self.As_Espadas)
elif jogo.mao_2[0] == "Ás Copas":
    screen.carta_1_jogador_1.configure(image= self.As_Copas)
elif jogo.mao_2[0] == "Ás Paus":
    screen.carta_1_jogador_1.configure(image= self.As_Paus)
elif jogo.mao_2[0] == "Dois Ouros":
    screen.carta_1_jogador_1.configure(image= self.Dois_Ouros)
elif jogo.mao_2[0] == "Dois Ouros":
    screen.carta_1_jogador_1.configure(image= self.Dois_Espadas)
elif jogo.mao_2[0] == "Dois Espadas":
    screen.carta_1_jogador_1.configure(image= self.Dois_Copas)
elif jogo.mao_2[0] == "Dois Paus":
    screen.carta_1_jogador_1.configure(image= self.Dois_Paus)
elif jogo.mao_2[0] == "Tres Ouros":
    screen.carta_1_jogador_1.configure(image= self.Tres_Ouros)
elif jogo.mao_2[0] == "Tres Espadas":
    screen.carta_1_jogador_1.configure(image= self.Tres_Espadas)
elif jogo.mao_2[0] == "Tres Copas":
    screen.carta_1_jogador_1.configure(image= self.Tres_Copas)
elif jogo.mao_2[0] == "Tres Paus":
    screen.carta_1_jogador_1.configure(image= self.Tres_Paus)
elif jogo.mao_2[0] == "Quatro Ouros":
    screen.carta_1_jogador_1.configure(image= self.Quatro_Ouros)
elif jogo.mao_2[0] == "Quatro Espadas":
    screen.carta_1_jogador_1.configure(image= self.Quatro_Espadas)
elif jogo.mao_2[0] == "Quatro Copas":
    screen.carta_1_jogador_1.configure(image= self.Quatro_Copas)
elif jogo.mao_2[0] == "Quatro Paus":
    screen.carta_1_jogador_1.configure(image= self.Quatro_Paus)
elif jogo.mao_2[0] == "Cinco Ouros":
    screen.carta_1_jogador_1.configure(image= self.Cinco_Ouros)
elif jogo.mao_2[0] == "Cinco Espadas":
    screen.carta_1_jogador_1.configure(image= self.Cinco_Espadas)
elif jogo.mao_2[0] == "Cinco Copas":
    screen.carta_1_jogador_1.configure(image= self.Cinco_Copas)
elif jogo.mao_2[0] == "Cinco Paus":
    screen.carta_1_jogador_1.configure(image= self.Cinco_Paus)
elif jogo.mao_2[0] == "Seis Ouros":
    screen.carta_1_jogador_1.configure(image= self.Seis_Ouros)
elif jogo.mao_2[0] == "Seis Espadas":
    screen.carta_1_jogador_1.configure(image= self.Seis_Espadas)
elif jogo.mao_2[0] == "Seis Copas":
    screen.carta_1_jogador_1.configure(image= self.Seis_Copas)
elif jogo.mao_2[0] == "Seis Paus":
    screen.carta_1_jogador_1.configure(image= self.Seis_Paus)
elif jogo.mao_2[0] == "Sete Ouros":
    screen.carta_1_jogador_1.configure(image= self.Sete_Ouros)
elif jogo.mao_2[0] == "Sete Espadas":
    screen.carta_1_jogador_1.configure(image= self.Sete_Espadas)
elif jogo.mao_2[0] == "Sete Copas":
    screen.carta_1_jogador_1.configure(image= self.Sete_Copas)
elif jogo.mao_2[0] == "Sete Paus":
    screen.carta_1_jogador_1.configure(image= self.Sete_Paus)
elif jogo.mao_2[0] == "Dama Ouros":
    screen.carta_1_jogador_1.configure(image= self.Dama_Ouros)
elif jogo.mao_2[0] == "Dama Espadas":
    screen.carta_1_jogador_1.configure(image= self.Dama_Espadas)
elif jogo.mao_2[0] == "Dama Copas":
    screen.carta_1_jogador_1.configure(image= self.Dama_Copas)
elif jogo.mao_2[0] == "Dama Paus":
    screen.carta_1_jogador_1.configure(image= self.Dama_Paus)
elif jogo.mao_2[0] == "Valete Ouros":
    screen.carta_1_jogador_1.configure(image= self.Valete_Ouros)
elif jogo.mao_2[0] == "Valete Espadas":
    screen.carta_1_jogador_1.configure(image= self.Valete_Espadas)
elif jogo.mao_2[0] == "Valete Copas":
    screen.carta_1_jogador_1.configure(image= self.Valete_Copas)
elif jogo.mao_2[0] == "Valete Paus":
    screen.carta_1_jogador_1.configure(image= self.Valete_Paus)
elif jogo.mao_2[0] == "Rei Ouros":
    screen.carta_1_jogador_1.configure(image= self.Rei_Ouros)
elif jogo.mao_2[0] == "Rei Espadas":
    screen.carta_1_jogador_1.configure(image= self.Rei_Espadas)
elif jogo.mao_2[0] == "Rei Copas":
    screen.carta_1_jogador_1.configure(image= self.Rei_Copas)
elif jogo.mao_2[0] == "Rei Paus":
    screen.carta_1_jogador_1.configure(image= self.Rei_Paus)

    #Colocando a segunda carta do jogador 2 no Layout

if jogo.mao_2[1] == "Ás Ouros":
    screen.carta_1_jogador_1.configure(image=self.As_Ouros)
elif jogo.mao_2[1] == "Ás Espadas":
    screen.carta_1_jogador_1.configure(image= self.As_Espadas)
elif jogo.mao_2[1] == "Ás Copas":
    screen.carta_1_jogador_1.configure(image= self.As_Copas)
elif jogo.mao_2[1] == "Ás Paus":
    screen.carta_1_jogador_1.configure(image= self.As_Paus)
elif jogo.mao_2[1] == "Dois Ouros":
    screen.carta_1_jogador_1.configure(image= self.Dois_Ouros)
elif jogo.mao_2[1] == "Dois Ouros":
    screen.carta_1_jogador_1.configure(image= self.Dois_Espadas)
elif jogo.mao_2[1] == "Dois Espadas":
    screen.carta_1_jogador_1.configure(image= self.Dois_Copas)
elif jogo.mao_2[1] == "Dois Paus":
    screen.carta_1_jogador_1.configure(image= self.Dois_Paus)
elif jogo.mao_2[1] == "Tres Ouros":
    screen.carta_1_jogador_1.configure(image= self.Tres_Ouros)
elif jogo.mao_2[1] == "Tres Espadas":
    screen.carta_1_jogador_1.configure(image= self.Tres_Espadas)
elif jogo.mao_2[1] == "Tres Copas":
    screen.carta_1_jogador_1.configure(image= self.Tres_Copas)
elif jogo.mao_2[1] == "Tres Paus":
    screen.carta_1_jogador_1.configure(image= self.Tres_Paus)
elif jogo.mao_2[1] == "Quatro Ouros":
    screen.carta_1_jogador_1.configure(image= self.Quatro_Ouros)
elif jogo.mao_2[1] == "Quatro Espadas":
    screen.carta_1_jogador_1.configure(image= self.Quatro_Espadas)
elif jogo.mao_2[1] == "Quatro Copas":
    screen.carta_1_jogador_1.configure(image= self.Quatro_Copas)
elif jogo.mao_2[1] == "Quatro Paus":
    screen.carta_1_jogador_1.configure(image= self.Quatro_Paus)
elif jogo.mao_2[1] == "Cinco Ouros":
    screen.carta_1_jogador_1.configure(image= self.Cinco_Ouros)
elif jogo.mao_2[1] == "Cinco Espadas":
    screen.carta_1_jogador_1.configure(image= self.Cinco_Espadas)
elif jogo.mao_2[1] == "Cinco Copas":
    screen.carta_1_jogador_1.configure(image= self.Cinco_Copas)
elif jogo.mao_2[1] == "Cinco Paus":
    screen.carta_1_jogador_1.configure(image= self.Cinco_Paus)
elif jogo.mao_2[1] == "Seis Ouros":
    screen.carta_1_jogador_1.configure(image= self.Seis_Ouros)
elif jogo.mao_2[1] == "Seis Espadas":
    screen.carta_1_jogador_1.configure(image= self.Seis_Espadas)
elif jogo.mao_2[1] == "Seis Copas":
    screen.carta_1_jogador_1.configure(image= self.Seis_Copas)
elif jogo.mao_2[1] == "Seis Paus":
    screen.carta_1_jogador_1.configure(image= self.Seis_Paus)
elif jogo.mao_2[1] == "Sete Ouros":
    screen.carta_1_jogador_1.configure(image= self.Sete_Ouros)
elif jogo.mao_2[1] == "Sete Espadas":
    screen.carta_1_jogador_1.configure(image= self.Sete_Espadas)
elif jogo.mao_2[1] == "Sete Copas":
    screen.carta_1_jogador_1.configure(image= self.Sete_Copas)
elif jogo.mao_2[1] == "Sete Paus":
    screen.carta_1_jogador_1.configure(image= self.Sete_Paus)
elif jogo.mao_2[1] == "Dama Ouros":
    screen.carta_1_jogador_1.configure(image= self.Dama_Ouros)
elif jogo.mao_2[1] == "Dama Espadas":
    screen.carta_1_jogador_1.configure(image= self.Dama_Espadas)
elif jogo.mao_2[1] == "Dama Copas":
    screen.carta_1_jogador_1.configure(image= self.Dama_Copas)
elif jogo.mao_2[1] == "Dama Paus":
    screen.carta_1_jogador_1.configure(image= self.Dama_Paus)
elif jogo.mao_2[1] == "Valete Ouros":
    screen.carta_1_jogador_1.configure(image= self.Valete_Ouros)
elif jogo.mao_2[1] == "Valete Espadas":
    screen.carta_1_jogador_1.configure(image= self.Valete_Espadas)
elif jogo.mao_2[1] == "Valete Copas":
    screen.carta_1_jogador_1.configure(image= self.Valete_Copas)
elif jogo.mao_2[1] == "Valete Paus":
    screen.carta_1_jogador_1.configure(image= self.Valete_Paus)
elif jogo.mao_2[1] == "Rei Ouros":
    screen.carta_1_jogador_1.configure(image= self.Rei_Ouros)
elif jogo.mao_2[1] == "Rei Espadas":
    screen.carta_1_jogador_1.configure(image= self.Rei_Espadas)
elif jogo.mao_2[1] == "Rei Copas":
    screen.carta_1_jogador_1.configure(image= self.Rei_Copas)
elif jogo.mao_2[1] == "Rei Paus":
    screen.carta_1_jogador_1.configure(image= self.Rei_Paus)

    #Colocando a terceira carta do jogador 2 no Layout

if jogo.mao_2[2] == "Ás Ouros":
    screen.carta_1_jogador_1.configure(image=self.As_Ouros)
elif jogo.mao_2[2] == "Ás Espadas":
    screen.carta_1_jogador_1.configure(image= self.As_Espadas)
elif jogo.mao_2[2] == "Ás Copas":
    screen.carta_1_jogador_1.configure(image= self.As_Copas)
elif jogo.mao_2[2] == "Ás Paus":
    screen.carta_1_jogador_1.configure(image= self.As_Paus)
elif jogo.mao_2[2] == "Dois Ouros":
    screen.carta_1_jogador_1.configure(image= self.Dois_Ouros)
elif jogo.mao_2[2] == "Dois Ouros":
    screen.carta_1_jogador_1.configure(image= self.Dois_Espadas)
elif jogo.mao_2[2] == "Dois Espadas":
    screen.carta_1_jogador_1.configure(image= self.Dois_Copas)
elif jogo.mao_2[2] == "Dois Paus":
    screen.carta_1_jogador_1.configure(image= self.Dois_Paus)
elif jogo.mao_2[2] == "Tres Ouros":
    screen.carta_1_jogador_1.configure(image= self.Tres_Ouros)
elif jogo.mao_2[2] == "Tres Espadas":
    screen.carta_1_jogador_1.configure(image= self.Tres_Espadas)
elif jogo.mao_2[2] == "Tres Copas":
    screen.carta_1_jogador_1.configure(image= self.Tres_Copas)
elif jogo.mao_2[2] == "Tres Paus":
    screen.carta_1_jogador_1.configure(image= self.Tres_Paus)
elif jogo.mao_2[2] == "Quatro Ouros":
    screen.carta_1_jogador_1.configure(image= self.Quatro_Ouros)
elif jogo.mao_2[2] == "Quatro Espadas":
    screen.carta_1_jogador_1.configure(image= self.Quatro_Espadas)
elif jogo.mao_2[2] == "Quatro Copas":
    screen.carta_1_jogador_1.configure(image= self.Quatro_Copas)
elif jogo.mao_2[2] == "Quatro Paus":
    screen.carta_1_jogador_1.configure(image= self.Quatro_Paus)
elif jogo.mao_2[2] == "Cinco Ouros":
    screen.carta_1_jogador_1.configure(image= self.Cinco_Ouros)
elif jogo.mao_2[2] == "Cinco Espadas":
    screen.carta_1_jogador_1.configure(image= self.Cinco_Espadas)
elif jogo.mao_2[2] == "Cinco Copas":
    screen.carta_1_jogador_1.configure(image= self.Cinco_Copas)
elif jogo.mao_2[2] == "Cinco Paus":
    screen.carta_1_jogador_1.configure(image= self.Cinco_Paus)
elif jogo.mao_2[2] == "Seis Ouros":
    screen.carta_1_jogador_1.configure(image= self.Seis_Ouros)
elif jogo.mao_2[2] == "Seis Espadas":
    screen.carta_1_jogador_1.configure(image= self.Seis_Espadas)
elif jogo.mao_2[2] == "Seis Copas":
    screen.carta_1_jogador_1.configure(image= self.Seis_Copas)
elif jogo.mao_2[2] == "Seis Paus":
    screen.carta_1_jogador_1.configure(image= self.Seis_Paus)
elif jogo.mao_2[2] == "Sete Ouros":
    screen.carta_1_jogador_1.configure(image= self.Sete_Ouros)
elif jogo.mao_2[2] == "Sete Espadas":
    screen.carta_1_jogador_1.configure(image= self.Sete_Espadas)
elif jogo.mao_2[2] == "Sete Copas":
    screen.carta_1_jogador_1.configure(image= self.Sete_Copas)
elif jogo.mao_2[2] == "Sete Paus":
    screen.carta_1_jogador_1.configure(image= self.Sete_Paus)
elif jogo.mao_2[2] == "Dama Ouros":
    screen.carta_1_jogador_1.configure(image= self.Dama_Ouros)
elif jogo.mao_2[2] == "Dama Espadas":
    screen.carta_1_jogador_1.configure(image= self.Dama_Espadas)
elif jogo.mao_2[2] == "Dama Copas":
    screen.carta_1_jogador_1.configure(image= self.Dama_Copas)
elif jogo.mao_2[2] == "Dama Paus":
    screen.carta_1_jogador_1.configure(image= self.Dama_Paus)
elif jogo.mao_2[2] == "Valete Ouros":
    screen.carta_1_jogador_1.configure(image= self.Valete_Ouros)
elif jogo.mao_2[2] == "Valete Espadas":
    screen.carta_1_jogador_1.configure(image= self.Valete_Espadas)
elif jogo.mao_2[2] == "Valete Copas":
    screen.carta_1_jogador_1.configure(image= self.Valete_Copas)
elif jogo.mao_2[2] == "Valete Paus":
    screen.carta_1_jogador_1.configure(image= self.Valete_Paus)
elif jogo.mao_2[2] == "Rei Ouros":
    screen.carta_1_jogador_1.configure(image= self.Rei_Ouros)
elif jogo.mao_2[2] == "Rei Espadas":
    screen.carta_1_jogador_1.configure(image= self.Rei_Espadas)
elif jogo.mao_2[2] == "Rei Copas":
    screen.carta_1_jogador_1.configure(image= self.Rei_Copas)
elif jogo.mao_2[2] == "Rei Paus":
    screen.carta_1_jogador_1.configure(image= self.Rei_Paus)

while jogo.resultado == 0:
    if jogo.jogador == 1:
        c = jogada(1, jogo.mao_1)
    else:
        c = jogada(2, jogo.mao_2)
    jogo.recebe_jogada(c)

print("Jogador {0} venceu!".format(jogo.resultado))