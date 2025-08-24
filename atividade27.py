
palavra = input("Digite uma palavra: ")
vogais = "aeiou"
contador_vogais = 0
for letra in palavra:
  if letra in vogais:
    contador_vogais += 1
print(f"A palavra '{palavra}' tem {contador_vogais} vogais.")