# lendo a string do usuário
string = input("Digite uma string: ")

# criando uma string vazia para armazenar a string invertida
invertida = ""

# percorrendo a string de trás para frente e adicionando cada caractere à string invertida
for i in range(len(string)-1, -1, -1):
    invertida += string[i]

# imprimindo a string invertida
print("A string invertida é:", invertida)
