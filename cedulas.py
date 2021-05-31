nota = int(input())
cedula = ['100', '50', '20', '10', '5', '2']

print("{} nota(s) de R$ 100".format(nota//int(cedula[0])))
valor = nota % 100
print("{} nota(s) de R$ 50".format(valor//int(cedula[1])))
valor %= 50
print("{} nota(s) de R$ 20".format(valor//int(cedula[2])))
valor %= 20
print("{} nota(s) de R$ 10".format(valor//int(cedula[3])))
valor %= 10
print("{} nota(s) de R$ 5".format(valor//int(cedula[4])))
valor %= 5
print("{} nota(s) de R$ 2".format(valor//int(cedula[5])))
valor %= 2
print("{} nota(s) de R$ 1".format(valor), end="")

