import re

frases = []

executando = True
while executando:
    while True:
        data = input(f"Informe uma palavra: ")

        if data == 'sair':
            executando = False
            break

        if not data:
            print(f"O valor informado é inválido")
        else:
            frases.append(data)
            break

for frase in frases:
    if bool(re.search(r'\beu\b', frase.lower())):
        print(f"A frase \"{frase}\" possui a sentença \"eu\"")