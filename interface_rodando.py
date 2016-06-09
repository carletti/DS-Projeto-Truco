import tkinter as tk
import truco_simples as ts

class Screen:
    
    def __init__(self):
        self.jogo = ts.Jogo()   
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
        
        # Criando os botões
        self.criar_botões()

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
<<<<<<< HEAD

        self.Fundo_Baralho=tk.PhotoImage(file= "Fundo_Baralho.png")        
=======
>>>>>>> origin/master
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

        # Dicionário com as strings das cartas como chave que irào retornar o valor "imagem das cartas"
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


    #Cartas (Botões)
    def criar_botões(self):
        self.carta_1_jogador_1 = tk.Button(self.screen)
        self.carta_1_jogador_1.configure(text = 'Carta 1', bg = 'green', command= self.carta_1_jogador_1_clicada, bd= 0)
        self.carta_1_jogador_1.grid(row = 1, column = 1, sticky= "nsew")
        
        self.carta_2_jogador_1 = tk.Button(self.screen)
        self.carta_2_jogador_1.configure(bg = 'green', text = 'Carta 2', command= self.carta_2_jogador_1_clicada, bd= 0)
        self.carta_2_jogador_1.grid(row = 1, column = 3, sticky= "nsew")
        
        self.carta_3_jogador_1 = tk.Button(self.screen)
        self.carta_3_jogador_1.configure(bg = 'green', text = 'Carta 3', command= self.carta_3_jogador_1_clicada, bd= 0)
        self.carta_3_jogador_1.grid(row = 1, column = 5, sticky= "nsew")

        self.carta_1_jogador_2 = tk.Button(self.screen)
        self.carta_1_jogador_2.grid(row = 5, column = 5, sticky= "nsew")
        self.carta_1_jogador_2.configure(bg = 'green', command= self.carta_1_jogador_2_clicada, bd= 0)
        
        self.carta_2_jogador_2 = tk.Button(self.screen)
        self.carta_2_jogador_2.grid(row = 5, column = 7, sticky= "nsew")
        self.carta_2_jogador_2.configure(bg = 'green', command= self.carta_2_jogador_2_clicada, bd= 0)
        
        self.carta_3_jogador_2 = tk.Button(self.screen)
        self.carta_3_jogador_2.grid(row = 5, column = 9, sticky= "nsew")
        self.carta_3_jogador_2.configure(bg = 'green', command= self.carta_3_jogador_2_clicada, bd= 0)

        # Label onde o nome dos jogadores irá aparecer
        self.jogador_2 = tk.Label(self.screen)
        self.jogador_2.grid(row= 5, column= 3, sticky= "nsew")
        self.jogador_2.configure(bg= "green", text= "Jogador 2", font= "arial 15 bold")

        self.jogador_1 = tk.Label(self.screen)
        self.jogador_1.grid(row= 1, column= 7, sticky= "nsew")
        self.jogador_1.configure(bg= "green", text= "Jogador 1", font= "arial 15 bold")

        # Label onde as cartas irão aparecer
        self.carta_jogada_jogador_1 = tk.Label()
        self.carta_jogada_jogador_1.configure(bg= "green")
        self.carta_jogada_jogador_1.grid(row= 3, column= 3, sticky= "nsew")

        self.carta_jogada_jogador_2 = tk.Label()
        self.carta_jogada_jogador_2.configure(bg= "green")
        self.carta_jogada_jogador_2.grid(column= 7, row= 3, sticky= "nsew")

        versus= tk.Label()
        versus.configure(text= "X", font= "arial 56 bold", bg= "green")
        versus.grid(row= 3, column= 5, sticky= "nsew")
        
    #Atribuir cartas aos botões
    def receber_imagens_jogador_1(self):
        # Imagens salvas para aparecer na label
        self.c1j1 = self.jogo.mao_1[0].carta_str()
        self.c2j1 = self.jogo.mao_1[1].carta_str()
        self.c3j1 = self.jogo.mao_1[2].carta_str()
        # Print de teste
        print(self.jogo.mao_1[0])
        print(self.jogo.mao_1[1])
        print(self.jogo.mao_1[2])
        self.carta_1_jogador_1.configure(image = self.imagens_carta[self.jogo.mao_1[0].carta_str()])
        self.carta_2_jogador_1.configure(image = self.imagens_carta[self.jogo.mao_1[1].carta_str()])
        self.carta_3_jogador_1.configure(image = self.imagens_carta[self.jogo.mao_1[2].carta_str()])
        

    def receber_imagens_jogador_2(self):
        self.c1j2 = self.jogo.mao_2[0].carta_str()
        self.c2j2 = self.jogo.mao_2[1].carta_str()
        self.c3j2 = self.jogo.mao_2[2].carta_str()
        
        print(self.jogo.mao_2[0])
        print(self.jogo.mao_2[1])
        print(self.jogo.mao_2[2])
        self.carta_1_jogador_2.configure(image = self.imagens_carta[self.jogo.mao_2[0].carta_str()])
        self.carta_2_jogador_2.configure(image = self.imagens_carta[self.jogo.mao_2[1].carta_str()])
        self.carta_3_jogador_2.configure(image = self.imagens_carta[self.jogo.mao_2[2].carta_str()])
            
    #Criando os Callbacks dos botões

    def carta_1_jogador_1_clicada(self):
        self.carta_1_jogador_1.configure(bg="green", state= "disabled", bd= 0, text= "")
        self.jogo.recebe_jogada(0)
        print(self.jogo.mao_1[0])
        self.carta_jogada_jogador_1.configure(image= self.imagens_carta[self.c1j1])

    def carta_2_jogador_1_clicada(self):
        self.carta_2_jogador_1.configure(bg="green", state= "disabled", bd= 0, text= "")
        self.jogo.recebe_jogada(1)
        print(self.jogo.mao_1[1])
        self.carta_jogada_jogador_1.configure(image = self.imagens_carta[self.c2j1])

    def carta_3_jogador_1_clicada(self):
        self.carta_3_jogador_1.configure(bg="green", state= "disabled", bd= 0, text= "")
        self.jogo.recebe_jogada(2)
        print(self.jogo.mao_1[2])    
        self.carta_jogada_jogador_1.configure(image= self.imagens_carta[self.c3j1])

    def carta_1_jogador_2_clicada(self):
        self.carta_1_jogador_2.configure(bg="green", state= "disabled", bd= 0, text= "")
        self.jogo.recebe_jogada(0)
        print(self.jogo.mao_2[0])
        self.carta_jogada_jogador_2.configure(image= self.imagens_carta[self.c1j2])

    def carta_2_jogador_2_clicada(self):
        self.carta_2_jogador_2.configure(bg="green", state= "disabled", bd= 0, text= "")    
        self.jogo.recebe_jogada(1)
        print(self.jogo.mao_2[1])
        self.carta_jogada_jogador_2.configure(image= self.imagens_carta[self.c2j2])

    def carta_3_jogador_2_clicada(self):
        self.carta_3_jogador_2.configure(bg="green", state= "disabled", bd= 0, text= "")
        self.jogo.recebe_jogada(2)
        print(self.jogo.mao_2[2])
        self.carta_jogada_jogador_2.configure(image= self.imagens_carta[self.c3j2])
        
    def reabilita_botão(self):
        self.criar_botões()
        
    def reinicia_rodada(self):
        self.jogo.inicia_round()        
        self.receber_imagens_jogador_1()
        self.receber_imagens_jogador_2()
#        
    def start(self):
        # while self.jogo.pontos_1 <= 12 or tself.jogo.pontos_2 <= 12:
            self.receber_imagens_jogador_1()
            self.receber_imagens_jogador_2()
#           self.reinicia_rodada()
            self.screen.mainloop()
            
    def esconde_cartas(self):
        if self.jogo.jogador == 1:
            self.carta_1_jogador_2.configure(image = self.Fundo_Baralho)
            self.carta_2_jogador_2.configure(image = self.Fundo_Baralho)
            self.carta_3_jogador_2.configure(image = self.Fundo_Baralho)
        elif self.jogo.jogador == 2:
            self.carta_2_jogador_1.configure(image = self.Fundo_Baralho)
            self.carta_2_jogador_1.configure(image = self.Fundo_Baralho)
            self.carta_2_jogador_1.configure(image = self.Fundo_Baralho)

app = Screen()

# while ts.jogo.pontos_1 <= 12 or ts.jogo.pontos_2 <= 12:
app.start()
while ts.Jogo.resultado == 0:
    if ts.Jogo.jogador == 1:
        c = ts.Jogo.jogada(1, ts.Jogo.mao_1)
    else:
        c = ts.Jogo.jogada(2, ts.Jogo.mao_2)
    ts.Jogo.recebe_jogada(c)

print("Jogador {0} venceu!".format(ts.Jogo.resultado))
