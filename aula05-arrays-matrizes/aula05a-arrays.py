lista_frutas = ["Maçã", "Morango", "Uva"]

# lista_frutas[0] = "Maçã"
# lista_frutas[1] = "Morango"
# lista_frutas[2] = "Uva"
print(lista_frutas[1])

lista_frutas.append("Jabuticaba")
print(lista_frutas[-1])
print()

tamanho = len(lista_frutas)

for i in range(tamanho):
    print(lista_frutas[i])

print()

for fruta in lista_frutas:
    print(fruta)

print()

msg = "Oi fulano!"

for i in range(len(msg)):
    print(msg[i])