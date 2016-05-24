# -*- coding: utf-8 -*-
"""
Created on Thu May 19 15:09:00 2016

@author: dell
"""

import pickle

arquivo = open("cadastrados.pickle", "wb")

cadastrados = dict()

pickle.dump(cadastrados, arquivo)

arquivo.close()