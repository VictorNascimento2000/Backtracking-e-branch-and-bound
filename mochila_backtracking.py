import numpy as np
import time

start = time.process_time()

#Abrindo o arquivo
file = open("items.csv")
items = np.loadtxt(file, delimiter=" ")

#Separando o número de items o peso de restrição
N = int(items[0][0])
W = items[0][1]

#Criando a matriz com os valores e adicionando uma coluna referente ao valor por peso
items = np.delete(items, 0, 0)
valuePerWeight = np.zeros((np.shape(items)[0], 1))
for i in range(N):
    valuePerWeight[i][0] = items[i][0]/items[i][1]
items = np.c_[items, valuePerWeight]

#ordenando as linhas da matriz em ordem decrescente em relação ao valor por peso dos items
ind = np.argsort(items[:,2])
rind = ind[::-1]
items = items[rind]

class Node:
    def __init__(self, level, value, weight):
        self.level = level
        self.value = value
        self.weight = weight

root = Node(0,0,0)
stack = []
stack.append(root)
best = 0
while len(stack) > 0:
    node = stack.pop()
    if node.level == N:
        if best < node.value:
            best = node.value
    else:
        x = Node(node.level+1, node.value, node.weight)
        stack.append(x)

        if node.weight + items[node.level][1] <= W:
            v = Node(node.level+1, node.value + items[node.level][0], node.weight + items[node.level][1])
            stack.append(v)
    
print(time.process_time() - start, end = '\n')
print(best)