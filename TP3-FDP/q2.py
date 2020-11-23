numeros = []
for i in range(1, 6):

    while True:
        data = input(f"Informe um número inteiro: ")
        data = int(data) if data.isnumeric() else False

        if not data:
            print(f"O valor informado é inválido")
        else:
            numeros.append(data)
            break

print(numeros)
