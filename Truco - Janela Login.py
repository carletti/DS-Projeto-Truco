# -*- coding: utf-8 -*-

import tkinter as tk
cadastrados = dict()

class janela_login():
    
    def __init__(self):
        
        #Criando Janela do Jogo
        self.login_cadastro = tk.Tk()
        self.login_cadastro.title("Truco")
        self.login_cadastro.geometry("750x600+200+40")
        self.login_cadastro.configure(background = "green")
        #Definindo Layout da Janela
        
        #Linhas
        self.login_cadastro.rowconfigure(0, minsize= 40, weight=1)
        self.login_cadastro.rowconfigure(1, minsize=40, weight=1)
        self.login_cadastro.rowconfigure(2, minsize= 40, weight=1)
        self.login_cadastro.rowconfigure(3, minsize= 40, weight=1)
        self.login_cadastro.rowconfigure(4, minsize= 40, weight=1)        
        self.login_cadastro.rowconfigure(5, minsize= 10, weight=1)
        self.login_cadastro.rowconfigure(6, minsize= 40, weight=1)       
        self.login_cadastro.rowconfigure(7, minsize= 30, weight=1)
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

        self.truco_label= tk.Label(self.login_cadastro)
        self.truco_label.configure(text= "TRUCO", fg= "white", font= "arial 60 bold", bg= "green")
        self.truco_label.grid(row= 0, column=1, sticky="nsew")

        self.naipes_inicio = tk.PhotoImage(file= "naipes inicial.png")
        self.label_naipes_inicio = tk.Label(self.login_cadastro, image= self.naipes_inicio, height= 0, width= 0, bg= "green")
        self.label_naipes_inicio.grid(row= 1, column= 1, sticky="nsew")
        
        #Criando espaço para colocar os dados de login

        self.texto_nome_login = tk.Label(self.login_cadastro)
        self.texto_nome_login.configure(text= "Usuário:", fg= "black", font= "Arial, 14", bg= "green")
        self.texto_nome_login.grid(row= 3, column= 0)
        self.nome_login = tk.Entry(self.login_cadastro)
        self.nome_login.configure(text= "Nome", bg= "light gray", bd= 3)
        self.nome_login.grid(row= 3, column= 1, sticky= "nsew")                
        
        self.texto_senha_login = tk.Label(self.login_cadastro)
        self.texto_senha_login.configure(text= "Senha do Usuário:", fg= "black", font= "Arial, 14", bg= "green")
        self.texto_senha_login.grid(row= 4, column= 0)
        self.senha_login = tk.Entry(self.login_cadastro)
        self.senha_login.configure(text= "Senha", bg= "light gray", bd= 3, show="•")
        self.senha_login.grid(row= 4, column= 1, sticky= "nsew")
        self.senha_login.bind("<Return>", self.apertou_enter_login)
        
        #Criando espaço para colocar os dados de Cadastro        

        self.texto_nome_cadastro = tk.Label(self.login_cadastro)
        self.texto_nome_cadastro.configure(text= "Nome do Usuário:", fg= "black", font= "Arial, 14", bg= "green")
        self.texto_nome_cadastro.grid(row= 8, column= 0)
        self.nome_cadastro = tk.Entry(self.login_cadastro)
        self.nome_cadastro.configure(text= "Nome Cadastro", bg= "light gray", bd= 3)
        self.nome_cadastro.grid(row= 8, column= 1, sticky= "nsew")        

        self.texto_senha_cadastro = tk.Label(self.login_cadastro)
        self.texto_senha_cadastro.configure(text= "Senha do Usuário:", fg= "black", font= "Arial, 14", bg= "green")
        self.texto_senha_cadastro.grid(row= 9, column= 0)
        self.senha_cadastro = tk.Entry(self.login_cadastro)
        self.senha_cadastro.configure(text= "Senha Cadastro", bg= "light gray", bd= 3, show="•")
        self.senha_cadastro.grid(row= 9, column= 1, sticky= "nsew")
        self.senha_cadastro.bind("<Return>", self.apertou_enter_cadastro)        
        
        #Criando botões Login e Cadastrar
 
        self.botao_login = tk.Button(self.login_cadastro)
        self.botao_login.grid(row= 6, column=1, sticky="nsew")
        self.botao_login.configure(background = "grey")        
        self.botao_login.configure(text = "Login", font= "Arial, 20", command= self.login_clicado)
 
 
        self.botao_cadastrar = tk.Button(self.login_cadastro)
        self.botao_cadastrar.grid(row=11 , column= 1, sticky="nsew")
        self.botao_cadastrar.configure(background = "grey")
        self.botao_cadastrar.configure(text = "Cadastre-se", font= "Arial, 20", command=self.cadastro_clicado)
    
    #Criando funções

    def cadastro_clicado(self):
        nome = self.nome_cadastro.get()
        senha = self.senha_cadastro.get()
        if nome in cadastrados:
            self.texto_nome_cadastro.configure(text= "Este Apelido já está em uso. Tente outro nome.")
        else:
            cadastrados[nome] = senha
            print (cadastrados)
        self.nome_cadastro.delete(0, 'end')
        self.senha_cadastro.delete(0, 'end')

    def login_clicado(self):
        nome = self.nome_login.get()
        senha = self.senha_login.get()
        if nome not in cadastrados:
            tk.messagebox.OK("Usu")
        if nome in cadastrados:
            senha_correta = cadastrados[nome]
            if senha == senha_correta:
                print ("Acesso liberado")
            else:
                tk.tkMessageBox.showinfo("Senha Incorreta")
        self.nome_login.delete(0, 'end')
        self.senha_login.delete(0,'end')


    def apertou_enter_login(self, event):
        self.login_clicado()
    
    def apertou_enter_cadastro(self, event):
        self.cadastro_clicado()

    #Iniciando a Janela
    def inicio(self):
        self.login_cadastro.mainloop()

janela= janela_login()
janela.inicio()
