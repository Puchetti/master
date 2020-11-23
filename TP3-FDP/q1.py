lista = []

for n in range(1, 6):
    lista.append(n)

print(lista)

for n in [3, 6]:
    if n in lista:
        lista.remove(n)

print(lista, '-> Tamanho:', len(lista), 'itens')

lista[-1] = 6
print(lista)