# -*- coding: utf-8 -*-

import tkinter as tk

class janela_login():
    
    def __init__(self):
        
        #Criando Janela do Jogo
        self.login_cadastro = tk.Tk()
        self.login_cadastro.title("Truco")
        self.login_cadastro.geometry("600x600+150+150")
        
        #Definindo Layout da Janela
        
        #Linhas
        self.login_cadastro.rowconfigure(0, minsize= 210)
        self.login_cadastro.rowconfigure(1, minsize= 100)        
        self.login_cadastro.rowconfigure(2, minsize= 75)
        self.login_cadastro.rowconfigure(3, minsize= 50)       
        self.login_cadastro.rowconfigure(4, minsize= 75)
        self.login_cadastro.rowconfigure(5, minsize= 90)
        self.login_cadastro.configure(background = "blue")        
        
        #Colunas
        self.login_cadastro.columnconfigure(0, minsize= 100)
        self.login_cadastro.columnconfigure(1, minsize= 400)
        self.login_cadastro.columnconfigure(2, minsize= 100)
        
        #Criando botões Login e Cadastrar
        self.botao_login = tk.Button(self.login_cadastro)
        self.botao_login.grid(row= 2, column=1, sticky="nsew")
        self.botao_login.configure(background = "light grey")        
        self.botao_login.configure(text = "Login")
 
        self.botao_cadastrar = tk.Button(self.login_cadastro)
        self.botao_cadastrar.grid(row=4 , column= 1, sticky="nsew")
        self.botao_cadastrar.configure(background = "light grey")
        self.botao_cadastrar.configure(text = "Cadastre-se")
   #Iniciando a Janela
    def inicio(self):
        self.login_cadastro.mainloop()

janela= janela_login()
janela.inicio()