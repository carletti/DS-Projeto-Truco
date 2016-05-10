# -*- coding: utf-8 -*-
import tkinter as tk

class Screen:
    def __init__(self):
        self.screen = tk.Tk()        
        self.screen.title('Truco')
        self.screen.geometry('800x600+300+50')
        self.screen.configure(bg = "darkgreen")
        
        #layout
        self.screen.rowconfigure(0, minsize = 200, weight = 1)
        self.screen.rowconfigure(1, minsize = 200, weight = 1)
        self.screen.rowconfigure(2, minsize = 200, weight = 1)
        self.screen.columnconfigure(0, minsize = 200, weight = 1)
        self.screen.columnconfigure(1, minsize = 200, weight = 1)
        self.screen.columnconfigure(2, minsize = 200, weight = 1)
        self.screen.columnconfigure(3, minsize = 200, weight = 1)
    
        #Cards
        card_1 = tk.Button(self.screen)
        card_1.configure(text = 'Carta 1')
        card_1.configure(width = 18, height = 150)
        card_1.configure(bg = 'white')
        card_1.grid(row = 2, column = 1)
        
        card_2 = tk.Button(self.screen)
        card_2.configure(text = 'Carta 2')
        card_2.configure(width = 18, height = 150)
        card_2.configure(bg = 'white')
        card_2.grid(row = 2, column = 2)
        
        card_3 = tk.Button(self.screen)
        card_3.configure(text = 'Carta 3')
        card_3.configure(width = 18, height = 150)
        card_3.configure(bg = 'white')
        card_3.grid(row = 2, column = 3)
        
        #Botão para pedir TRUCO!
        truco = tk.Button(self.screen)
        truco.configure(text = 'TRUCO !')
        truco.configure(width = 15, height = 5)
        truco.configure(bg = 'red')
        truco.grid(row = 2, column = 0)
        
        #Displays - em canvas
        display_1 = tk.Canvas(self.screen)
        display_1.grid(row = 0, column = 0)
        display_1.configure(width = 90, height = 150, bg = 'yellow')
        
        display_2 = tk.Canvas(self.screen)
        display_2.grid(row = 0, column = 1)
        display_2.configure(width = 90, height = 150, bg = 'yellow')
        
        display_3 = tk.Canvas(self.screen)
        display_3.grid(row = 0, column = 2)
        display_3.configure(width = 90, height = 150, bg = 'yellow')
        
        display_4 = tk.Canvas(self.screen)
        display_4.grid(row = 0, column = 3)
        display_4.configure(width = 90, height = 150, bg = 'yellow')
        
        vira = tk.Canvas(self.screen)
        vira.grid(row = 1, column = 0)
        vira.configure(width = 90, height = 150, bg = 'blue')
        
        
        
        
    def start(self):
        self.screen.mainloop()

app = Screen()
app.start()