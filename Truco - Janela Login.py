# -*- coding: utf-8 -*-

import tkinter as tk

class janela_login():
    
    def __init__(self):
        
        #Criando Janela do Jogo
        self.login_cadastro = tk.Tk()
        self.login_cadastro.title("Truco")
        self.login_cadastro.geometry("450x400+150+150")
        
        #Definindo Layout da Janela
        
        #Linhas
        self.login_cadastro.rowconfigure(0, minsize= 50)
        self.login_cadastro.rowconfigure(1, minsize= )        
        
        
        #Colunas
        self.login_cadastro.columnconfigure(0, minsize= 50)
        self.login_cadastro.columnconfigure(1, minsize= 400)
        self.login_cadastro.columnconfigure(2, minsize= 50)
    
        #Criando botões Login e Cadastrar
        self.botao_login = tk.Button(self.login_cadastro)
        self.botao_login.grid = (row= 1,)

        self.botao_cadastrar = tk.Button(self.login_cadastro)


   #Iniciando a Janela
    def inicio(self):
        self.login_cadastro.mainloop()
        