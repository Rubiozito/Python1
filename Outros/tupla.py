def compara_elementos(tupla):
    if tupla[-1] == tupla[0]:
        return True
    else:
        return False


tupla1 = 1, 2, 1
tupla2 = 1, 2, 3

print(compara_elementos(tupla1))
print(compara_elementos(tupla2))