# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 17:11:20 2021

@author: Patricia
"""
print= "Hello, World!"

idade= int(input("digite a idade:"))
if idade>=7 and idade<=9:
    print("infantil A")
elif idade>=8 and idade<= 12:
    print(" infantil B")
elif idade>=13 and idade<= 15:
    print("juvenil A")
elif idade>= 15 and idade<=17:
    print("juvenil B")
else:
    print("maior que 18 anos")
    
print("ate mais")