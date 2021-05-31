numero = input().split()
a, b, c = numero

maiorAB = (int(a) + int(b) + abs(int(a) - int(b)))/2
maior = (int(c) + (maiorAB) + abs(int(c) - (maiorAB)))/2
maior = int(maior)

print(maior, end="")
