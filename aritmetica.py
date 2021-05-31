int1 = int(input())
s1 = input()
int2 = int(input())
s2 = input()
int3 = int(input())

def operador(op, int1, int2):
    if op == "+":
        return int1+int2
    if op == "-":
        return int1-int2
    if op == "*":
        return int1*int2
    if int2 == 0:
        return "erro"
    return int1//int2

try:
    if s1 != "*" and s1 != "/" and (s2 == "*" or s2 == "/"):
        r2 = operador(s2, int2, int3)
        r1 = operador(s1, int1, r2)
        print(r1, end="")
    else:
        r1 = operador(s1, int1, int2)
        r2 = operador(s2, r1, int3)
        print(r2, end="")
except:
    print("erro", end="")




