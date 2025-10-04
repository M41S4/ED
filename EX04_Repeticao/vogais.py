palavra = input("digite a palavra")
contador=0

vogais = "aioue"
for letra in palavra:
  if letra in vogais:
    contador += 1

print(contador)