# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 02:30:09 2021

@author: Patricia
"""
#Algoritmo preco/produto e percentual desconto

preco = float(input("escreva o preco do produto: "))
percentual = float(input(" escreva o valor percentual de desconto: "))

desc = percentual/100
valor = preco*desc
valor a pagar = preco - valor

print("valor de desconto: $", valor)
print("valor a pagar: $",pagar)