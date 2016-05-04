# -*- coding: utf-8 -*-

import tkinter as tk

class janela_login():
    
    def __init__(self):
        
        #Criando Janela do Jogo
        self.login_cadastro = tk.Tk()
        self.login_cadastro.title("Truco")
        self.login_cadastro.geometry("750x600+150+150")
        
        #Definindo Layout da Janela
        
        #Linhas
        self.login_cadastro.rowconfigure(0, minsize= 40, weight=1)
        self.login_cadastro.rowconfigure(1, minsize=40, weight=1)
        self.login_cadastro.rowconfigure(2, minsize= 40, weight=1)
        self.login_cadastro.rowconfigure(3, minsize= 40, weight=1)
        self.login_cadastro.rowconfigure(4, minsize= 40, weight=1)        
        self.login_cadastro.rowconfigure(5, minsize= 10, weight=1)
        self.login_cadastro.rowconfigure(6, minsize= 40, weight=1)       
        self.login_cadastro.rowconfigure(7, minsize= 40, weight=1)
        self.login_cadastro.rowconfigure(8, minsize= 40, weight=1)
        self.login_cadastro.rowconfigure(9, minsize= 40, weight=1)
        self.login_cadastro.rowconfigure(10, minsize= 10, weight=1)
        self.login_cadastro.rowconfigure(11, minsize= 40, weight=1)
        self.login_cadastro.rowconfigure(12, minsize= 40, weight=1)
        self.login_cadastro.rowconfigure(13, weight=1)
        
        #Colunas
        self.login_cadastro.columnconfigure(0, minsize= 100, weight=1)
        self.login_cadastro.columnconfigure(1, minsize= 400, weight=1)
        self.login_cadastro.columnconfigure(2, minsize= 100, weight=1)
        
        self.login_cadastro.configure(background = "green")
        
        #Criando espaço para colocar os dados de login
        nome_login = tk.Entry(self.login_cadastro)
        nome_login.configure(text= "Nome", bg= "light gray", bd= 3)
        nome_login.grid(row= 3, column= 1, sticky= "nsew")        
        
        senha_login = tk.Entry(self.login_cadastro)
        senha_login.configure(text= "Senha", bg= "light gray", bd= 3)
        senha_login.grid(row= 4, column= 1, sticky= "nsew")
        
        #Criando espaço para colocar os dados de Cadastro        
        
        nome_cadastro = tk.Entry(self.login_cadastro)
        nome_cadastro.configure(text= "Nome Cadastro", bg= "light gray", bd= 3)
        nome_cadastro.grid(row= 8, column= 1, sticky= "nsew")        
        
        senha_cadastro = tk.Entry(self.login_cadastro)
        senha_cadastro.configure(text= "Senha Cadastro", bg= "light gray", bd= 3)
        senha_cadastro.grid(row= 9, column= 1, sticky= "nsew")
                
        
        #Criando botões Login e Cadastrar
 
        self.botao_login = tk.Button(self.login_cadastro)
        self.botao_login.grid(row= 6, column=1, sticky="nsew")
        self.botao_login.configure(background = "grey")        
        self.botao_login.configure(text = "Login")
 
        self.botao_cadastrar = tk.Button(self.login_cadastro)
        self.botao_cadastrar.grid(row=11 , column= 1, sticky="nsew")
        self.botao_cadastrar.configure(background = "grey")
        self.botao_cadastrar.configure(text = "Cadastre-se")
   
   #Iniciando a Janela
    def inicio(self):
        self.login_cadastro.mainloop()

janela= janela_login()
janela.inicio()