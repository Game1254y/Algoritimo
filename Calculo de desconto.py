valor = float(input("digite o valor da compra"))

if valor > 100:
    valor = valor - (valor * 0.10)
    print("valor com desconto:", valor)
else:
    print("não há desconto")