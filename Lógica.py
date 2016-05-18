# -*- coding: utf-8 -*-
import random

# Definindo cartas
class cartas:    
    def __init__(self, valor, naipe):
        self.valor = valor
        self.naipe = naipe

# Definindo baralho        
class baralho:
    
    def __init__(self):
        # Lista com o nome das cartas
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
                             'Três Paus',
                             'Manilha Ouros',
                             'Manilha Espada',
                             'Manilha Copas',
                             'Manilha Paus']
        # Lista com o número correspondente ao nome das cartas
        self.cartas = [x for x in range(44)]
        # Copiando as listas
        self.cartas_em_jogo = self.cartas[:]
        self.nome_cartas_em_jogo = self.nome_cartas[:]
    
    # Reconfigura a lista de números copiada de acordo com as original    
    def reiniciar_cartas_em_jogo(self):
        self.cartas_em_jogo = self.cartas[:]
        return self.cartas_em_jogo
    
    # Reconfigura a lista de números copiada de acordo com as original    
    def reiniciar_nome_cartas_em_jogo(self):
        self.nome_cartas_em_jogo = self.nome_cartas[:]
        return self.nome_cartas_em_jogo
 
    # Distribiu as cartas para os jogadores e gera o vira       
    def comprar_carta(self):
        i = random.randint(0, len(self.cartas_em_jogo)-5)
        print (i)
        print (self.cartas_em_jogo[i])
        print (self.nome_cartas_em_jogo[i])
        numero_carta = self.cartas_em_jogo[i]
        carta = self.nome_cartas_em_jogo[i]
        self.cartas_em_jogo.remove(numero_carta)
        self.nome_cartas_em_jogo.remove(carta)
        return [carta, numero_carta]
        
    # Chama a função comprar carta e coloca em um dicionário
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
baralho_de_truco.sortear()

print("BARALHO SORTEADO")
print(baralho_de_truco.sorteio)
print()

baralho_de_truco.reiniciar_nome_cartas_em_jogo()
print(baralho_de_truco.nome_cartas_em_jogo)
print()

baralho_de_truco.reiniciar_cartas_em_jogo()
print(baralho_de_truco.cartas_em_jogo)
print()

# Defini jogador
class jogador:

    def __init__(self, cartas, número):
        self.número = número
        self.cartas = cartas
        
        self.jogador_1 = [a[0]]
        self.jogador_2 = [a[1]]
        self.jogador_3 = [a[2]]
        self.jogador_4 = [a[3]]
        self.numero_vira = [a[4]]
    
    # Defini qual jogador esta com qual carta em coloca em uma lista     
    def define_jogador(self):
        self.na_mesa = []
        for i, j in s.items():
            self.na_mesa.append(j)
            print ('O jogador {0} tem as cartas {1}'.format(i, j))
        return self.na_mesa

# Teste            
jogadores_de_truco = jogador(s.keys, s.values)
a = jogadores_de_truco.define_jogador()
print('')
print(a)
print ('')

# Define mesa
class mesa:

    def __init__(self):
        self.jogador_1 = a[0][1]
        self.jogador_2 = a[1][1]
        self.jogador_3 = a[2][1]
        self.jogador_4 = a[3][1]
        self.numero_vira = a[4][1]
            
    # Define a manilha    
    def define_manilha(self):

        # Quando vira o vira é de our0s
        if self.numero_vira%4 == 0:
            baralho_de_truco.cartas_em_jogo[40] = self.numero_vira + 4
            baralho_de_truco.cartas_em_jogo[41] = self.numero_vira + 5
            baralho_de_truco.cartas_em_jogo[42] = self.numero_vira + 6
            baralho_de_truco.cartas_em_jogo[43] = self.numero_vira + 7
            return baralho_de_truco.cartas_em_jogo
        
        # Quando vira o vira é de espada
        elif self.numero_vira%4 == 1:
            baralho_de_truco.cartas_em_jogo[40] = self.numero_vira + 3
            baralho_de_truco.cartas_em_jogo[41] = self.numero_vira + 4
            baralho_de_truco.cartas_em_jogo[42] = self.numero_vira + 5
            baralho_de_truco.cartas_em_jogo[43] = self.numero_vira + 6
            return baralho_de_truco.cartas_em_jogo
       
        # Quando vira o vira é de copas
        elif self.numero_vira%4 == 2:
            baralho_de_truco.cartas_em_jogo[40] = self.numero_vira + 2
            baralho_de_truco.cartas_em_jogo[41] = self.numero_vira + 3
            baralho_de_truco.cartas_em_jogo[42] = self.numero_vira + 4
            baralho_de_truco.cartas_em_jogo[43] = self.numero_vira + 5
            return baralho_de_truco.cartas_em_jogo
           
        # Quando vira o vira é de paus
        elif self.numero_vira%4 == 3:
            baralho_de_truco.cartas_em_jogo[41] = self.numero_vira + 1
            baralho_de_truco.cartas_em_jogo[42] = self.numero_vira + 2
            baralho_de_truco.cartas_em_jogo[43] = self.numero_vira + 3
            baralho_de_truco.cartas_em_jogo[44] = self.numero_vira + 4
            return baralho_de_truco.cartas_em_jogo
         
        # Se der problema
        else:
            return -1
            

# Teste        
mesa_de_truco = mesa()
m = mesa_de_truco.define_manilha()
print(m)