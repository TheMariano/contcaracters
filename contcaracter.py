import sys, random, string
print("   [+] Cont Caracteres [+]")
print("   [ 1 ] > Contar Caracteres de uma texto ou palavra")
print("   [ 2 ] > Gerador de caracteres")
print("   [ 3 ] > Sair do programas")
print("")
print("By: TheMariano")
A = input("Alternativa: ")
if A == "1" or A == "01":
    caracteres = input("Digite ou cole o texto para contar caracteres e palavras: ")
    contcaracteres = len(caracteres)
    print(f"O texto ou palavra que você digitou tem {contcaracteres} caracteres!")
if A == "2" or A == "02":
    quantcaracteres = int(input("Digite quantos caracteres você quer: "))
    geradorcaracteres = random.sample(string.ascii_letters + string.digits, quantcaracteres)
    misturarcaracteres = ''.join(geradorcaracteres)
    print(f"Aqui está a quantidade de caracteres que você pediu {quantcaracteres}:")
    print(misturarcaracteres)
elif A == "3" or A == "3":
    sys.exit()