ano = int(input("digite um ano"))

if ano % 4 == 0 and ano % 100 != 0:
    print("ano bissexto")
elif ano % 400 == 0:
    print("ano bissexto")
else:
    print("ano nao é bissexto")