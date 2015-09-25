import matplotlib.pyplot as plt

#cartas embaralhadas
cartas = [11, 18, 3, 1, 16, 12, 6, 19, 5, 0, 14, 4, 17, 9, 13, 7, 10, 15, 2, 8]
#imprimir a lista cartas
print("lista original:", cartas)
#numero de cartas
n = 20

#plotamos um grafico com as infos originais
plt.figure()
plt.plot(range(n), cartas, 'ok')
plt.title("grafico lista original")
plt.xlabel("numero de cartas")
plt.ylabel("valores das cartas")
plt.savefig("bubble-inicio.png")

#percorre com o i
for i in range(0, n - 1, 1):
#percorre com o j
    for j in range(i + 1, n, 1): 
#teste das cartas sob a condicao de maior ou menor
        if cartas[i] > cartas[j]:
#variavel temporaria "temp" para guardar o valor da carta i
            temp = cartas[i]
#troca de valor entre as cartas i e j
            cartas[i] = cartas[j]
#incorporacao do valor da variavel temp para a carta j
            cartas[j] = temp
#imprimir no terminal o resultado
print("lista em ordem crescente:", cartas) 
#imprime os cinco maiores valores
print ("cinco maiores valores:", cartas[n: n - 5: -1])
#imprime os cinco menores valores
#print (cartas[20: 15: -1] 
print ("cinco menores valores:", cartas[0: 5: 1])

#plotamos um grafico com as infos ordenadas
plt.figure()
plt.plot(range(n), cartas, 'ok')
plt.title("grafico lista ordenada")
plt.xlabel("numero de cartas")
plt.ylabel("valores das cartas")
plt.savefig("bubble-fim.png")

print ("Matematica {} - Turma {}".format("Especial", 1))


