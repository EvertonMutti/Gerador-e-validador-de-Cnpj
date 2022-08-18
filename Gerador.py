# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 16:51:30 2022

@author: Everton Castro
"""
from random import randint
def SomadorCnpjPart1(CNPJ):
    soma = 0
    for i, l in enumerate(CNPJ, -5):
        soma += int(l) * (i*(-1))
        if i == -2:
            for a, b in enumerate(CNPJ[4:], -9):
                soma += int(b) * (a*(-1))
            break
    return soma

def SomadorCnpjPart2(CNPJ):
    soma = 0
    for i, l in enumerate(CNPJ, -6):
        soma += int(l) * (i*(-1))
        if i == -2:
            for a, b in enumerate(CNPJ[5:], -9):
                soma += int(b) * (a*(-1))
            break
    return soma

def Gerador(CNPJ):
    CNPJ += DoisUltimos(SomadorCnpjPart1(CNPJ))
    CNPJ += DoisUltimos(SomadorCnpjPart2(CNPJ))
    print(CNPJ)
    return CNPJ
        
    
def DoisUltimos(soma):
    comparador = 11 - (soma % 11) 
    if comparador > 9:
        return '0'
    else:
        return str(comparador)


if __name__ == '__main__':
    Gerador(str(randint(100000000000,999999999999)))



