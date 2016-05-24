# -*- coding: utf-8 -*-
import tkinter as tk
from truco_simples import Jogo
 

def compara_cartas(carta1, carta2):
    v1 = carta1.valor_carta()
    v2 = carta2.valor_carta()
    if v1 > v2:
        return 1
    else:
        return 2

<<<<<<< HEAD
class Baralho:
    def __init__(self):
<<<<<<< HEAD
        self.screen = tk.Tk()        
        self.screen.title('Truco')
        self.screen.geometry('800x640+300+50')
        self.screen.configure(bg = "darkgreen")
        
        #layout
        self.screen.rowconfigure(0, minsize = 40, weight = 1)
        self.screen.rowconfigure(1, minsize = 200, weight = 1)
        self.screen.rowconfigure(2, minsize = 200, weight = 1)
        self.screen.rowconfigure(3, minsize = 200, weight = 1)
        self.screen.columnconfigure(0, minsize = 200, weight = 1)
        self.screen.columnconfigure(1, minsize = 200, weight = 1)
        self.screen.columnconfigure(2, minsize = 200, weight = 1)
        self.screen.columnconfigure(3, minsize = 200, weight = 1)
    
        #Cards
        card_1 = tk.Button(self.screen)
        card_1.configure(text = 'Carta 1')
        card_1.configure(width = 18, height = 150)
        card_1.configure(bg = 'white')
        card_1.grid(row = 3, column = 1)
        
        card_2 = tk.Button(self.screen)
        card_2.configure(text = 'Carta 2')
        card_2.configure(width = 18, height = 150)
        card_2.configure(bg = 'white')
        card_2.grid(row = 3, column = 2)
        
        card_3 = tk.Button(self.screen)
        card_3.configure(text = 'Carta 3')
        card_3.configure(width = 18, height = 150)
        card_3.configure(bg = 'white')
        card_3.grid(row = 3, column = 3)
        
        #Botão para pedir TRUCO!
        truco = tk.Button(self.screen)
        truco.configure(text = 'TRUCO !')
        truco.configure(width = 15, height = 5)
        truco.configure(bg = 'red')
        truco.grid(row = 3, column = 0)
        
        #Displays - em canvas
        display_1 = tk.Canvas(self.screen)
        display_1.grid(row = 1, column = 0)
        display_1.configure(width = 90, height = 150, bg = 'yellow')
        
        display_2 = tk.Canvas(self.screen)
        display_2.grid(row = 1, column = 1)
        display_2.configure(width = 90, height = 150, bg = 'yellow')
        
        display_3 = tk.Canvas(self.screen)
        display_3.grid(row = 1, column = 2)
        display_3.configure(width = 90, height = 150, bg = 'yellow')
        
        display_4 = tk.Canvas(self.screen)
        display_4.grid(row = 1, column = 3)
        display_4.configure(width = 90, height = 150, bg = 'yellow')
        
        vira = tk.Canvas(self.screen)
        vira.grid(row = 2, column = 0)
        vira.configure(width = 90, height = 150, bg = 'blue')
        
        nome_1 = tk.Canvas(self.screen)
        nome_1.grid(row = 0, column = 0)
        nome_1.configure(width = 110, height = 30, bg = 'white')
        
        
        nome_2 = tk.Canvas(self.screen)
        nome_2.grid(row = 0, column = 1)
        nome_2.configure(width = 110, height = 30, bg = 'white')
        
        nome_3= tk.Canvas(self.screen)
        nome_3.grid(row = 0, column = 2)
        nome_3.configure(width = 110, height = 30, bg = 'white')
        
        nome_4 = tk.Canvas(self.screen)
        nome_4.grid(row = 0, column = 3)
        nome_4.configure(width = 110, height = 30, bg = 'white')
        
=======
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
            
=======

>>>>>>> 88869bed0e695742947be672db6feb1c75fe41d3
def jogada(jogador, mao):
      
    print("Cartas do jogador {0}".format(jogador))
    for carta in mao:
        print(carta, end=" ; ")
    print()
    c = int(input("Escolha sua carta: "))
    return c

class Screen:
    
    def __init__(self, jogo):
        self.jogo = Jogo()

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


        self.imagens_carta = {
            "Ás Ouros": self.As_Ouros ,
            "Ás Espadas": self.As_Espadas ,
            "Ás Copas": self.As_Copas ,
            "Ás Paus": self.As_Paus ,
            "Dois Ouros": self.Dois_Ouros ,
            "Dois Espadas": self.Dois_Espadas ,
            "Dois Copas": self.Dois_Copas ,
            "Dois Paus": self.Dois_Paus ,
            "Três Ouros": self.Tres_Ouros ,
            "Três Espadas": self.Tres_Espadas ,
            "Três Copas": self.Tres_Copas ,
            "Três Paus": self.Tres_Paus ,
            "Quatro Ouros": self.Quatro_Ouros ,
            "Quatro Espadas": self.Quatro_Espadas ,
            "Quatro Copas": self.Quatro_Copas ,
            "Quatro Paus": self.Quatro_Paus ,
            "Cinco Ouros": self.Cinco_Ouros ,
            "Cinco Espadas": self.Cinco_Espadas ,
            "Cinco Copas": self.Cinco_Copas ,
            "Cinco Paus": self.Cinco_Paus ,
            "Seis Ouros": self.Seis_Ouros ,
            "Seis Espadas": self.Seis_Espadas ,
            "Seis Copas": self.Seis_Copas ,
            "Seis Paus": self.Seis_Paus ,
            "Sete Ouros": self.Sete_Ouros ,
            "Sete Espadas": self.Sete_Espadas ,
            "Sete Copas": self.Sete_Copas ,
            "Sete Paus": self.Sete_Paus ,
            "Dama Ouros": self.Dama_Ouros ,
            "Dama Espadas": self.Dama_Espadas ,
            "Dama Copas": self.Dama_Copas ,
            "Dama Paus": self.Dama_Paus ,
            "Valete Ouros": self.Valete_Ouros ,
            "Valete Espadas": self.Valete_Espadas ,
            "Valete Copas": self.Valete_Copas ,
            "Valete Paus": self.Valete_Paus ,
            "Rei Ouros": self.Rei_Ouros ,
            "Rei Espadas": self.Rei_Espadas ,
            "Rei Copas": self.Rei_Copas ,
            "Rei Paus": self.Rei_Paus 
        }
        
        while self.jogo.resultado == 0:
            if self.jogo.jogador == 1:
                c = jogada(1, jogo.mao_1)

        #Cartas
                self.carta_1_jogador_1 = tk.Button(self.screen)
                self.carta_1_jogador_1.configure(text = 'Carta 1', bg = 'green', command= self.carta_1_jogador_1_clicada, bd= 0, image=self.imagens_carta[self.jogo.mao_2[0]])
                self.carta_1_jogador_1.grid(row = 1, column = 1, sticky= "nsew")
        
                self.carta_2_jogador_1 = tk.Button(self.screen)
                self.carta_2_jogador_1.configure(bg = 'green', text = 'Carta 2', command= self.carta_2_jogador_1_clicada, bd= 0, image=self.imagens_carta[self.jogo.mao_2[1]])
                self.carta_2_jogador_1.grid(row = 1, column = 3, sticky= "nsew")
        
                self.carta_3_jogador_1 = tk.Button(self.screen)
                self.carta_3_jogador_1.configure(bg = 'green', text = 'Carta 3', command= self.carta_3_jogador_1_clicada, bd= 0, image=self.imagens_carta[self.jogo.mao_2[2]])
                self.carta_3_jogador_1.grid(row = 1, column = 5, sticky= "nsew")

            else:
                c = jogada(2, jogo.mao_2)
                jogo.recebe_jogada(c)
        #Displays - em canvas
                self.carta_1_jogador_2 = tk.Button(self.screen)
                self.carta_1_jogador_2.grid(row = 5, column = 5, sticky= "nsew")
                self.carta_1_jogador_2.configure(bg = 'green', command= self.carta_1_jogador_2_clicada, bd= 0)
        
                self.carta_2_jogador_2 = tk.Button(self.screen)
                self.carta_2_jogador_2.grid(row = 5, column = 7, sticky= "nsew")
                self.carta_2_jogador_2.configure(bg = 'green', command= self.carta_2_jogador_2_clicada, bd= 0)
        
                self.carta_3_jogador_2 = tk.Button(self.screen)
                self.carta_3_jogador_2.grid(row = 5, column = 9, sticky= "nsew")
                self.carta_3_jogador_2.configure(bg = 'green', command= self.carta_3_jogador_2_clicada, bd= 0)

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
    

    def desenha_carta(self):
        self.carta_1_jogador_1.configure(
            image=self.imagens_carta[self.jogo.mao_1[0]])
        self.carta_2_jogador_1.configure(
            image=self.imagens_carta[self.jogo.mao_1[1]])
        self.carta_3_jogador_1.configure(
            image=self.imagens_carta[self.jogo.mao_1[2]])

        self.carta_1_jogador_2.configure(
            image=self.imagens_carta[self.jogo.mao_2[0]])
        self.carta_2_jogador_2.configure(
            image=self.imagens_carta[self.jogo.mao_2[1]])
        self.carta_3_jogador_2.configure(
            image=self.imagens_carta[self.jogo.mao_2[2]])

    #Criando os Callbacks dos botões

    def carta_1_jogador_1_clicada(self):
        self.carta_1_jogador_1.configure(bg="green", state= "disabled", bd= 0, text= "")
        self.jogo.recebe_jogada(0)

    def carta_2_jogador_1_clicada(self):
        self.carta_2_jogador_1.configure(bg="green", state= "disabled", bd= 0, text= "")
        self.jogo.recebe_jogada(1)

    def carta_3_jogador_1_clicada(self):
        self.carta_3_jogador_1.configure(bg="green", state= "disabled", bd= 0, text= "")
        self.jogo.recebe_jogada(2)

    def carta_1_jogador_2_clicada(self):
        self.carta_1_jogador_2.configure(bg="green", state= "disabled", bd= 0, text= "")
        self.jogo.recebe_jogada(0)

    def carta_2_jogador_2_clicada(self):
        self.carta_2_jogador_2.configure(bg="green", state= "disabled", bd= 0, text= "")    
        self.jogo.recebe_jogada(1)

    def carta_3_jogador_2_clicada(self):
        self.carta_3_jogador_2.configure(bg="green", state= "disabled", bd= 0, text= "")
        self.jogo.recebe_jogada(2)

    def start(self):
        self.screen.mainloop()

app = Screen()
app.start()
jogo = Jogo()

while jogo.resultado == 0:
    if jogo.jogador == 1:
        c = jogada(1, jogo.mao_1)
    else:
        c = jogada(2, jogo.mao_2)
    jogo.recebe_jogada(c)

print("Jogador {0} venceu!".format(jogo.resultado))