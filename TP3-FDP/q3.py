palavras = []
for i in range(1, 11):

    while True:
        data = input(f"Informe uma palavra: ")

        if not data:
            print(f"O valor informado é inválido")
        else:
            palavras.append(data)
            break

for palavra in palavras:
    print(palavra[::-1])