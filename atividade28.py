palavra = input("Digite uma palavra: ")

palavra_invertida = ""
for letra in palavra:
  palavra_invertida = letra + palavra_invertida
print(f"A palavra de trás para frente é: {palavra_invertida}")