n= int(input("Digite a quantidade de valores inteiros positivos: "))
valor= int(input("Digite os valores: "))
maior= valor
menor= valor
cont= 1

while cont < n:
    valor= int(input("Digite os valores: "))
    if valor < 0:
        break
    else:
        if valor < menor:
            menor= valor
        else:
            if valor > maior:
             maior= valor
            else:
                print("Valor invalido")
    cont= cont + 1    

print("Maior:", maior)
print("Menor: ", menor)



