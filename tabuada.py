#!/usr/bin/python3

__version__ = "0.1.0"
__author__ = "Juliene"

numeros = list(range(1, 11))

# Iterable (percorríveis)

for numero in numeros:
    print("Tabuada do:", numero)
    for numero_mult in numeros:
        print(numero * numero_mult)
    print("-------------")
