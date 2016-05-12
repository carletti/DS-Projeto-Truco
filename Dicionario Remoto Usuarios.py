# -*- coding: utf-8 -*-
"""
Created on Sun May  8 09:48:10 2016

@author: dell
"""
import pickle

usuarios = dict()
usuarios["Warlen"]="990505"
cadastro_usuarios = open("database.pickle, wb")
pickle.dump(usuarios, cadastro_usuarios)

cadastro_usuarios.close()

print (usuarios)