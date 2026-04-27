preco = float(input("Digite o Preço do produto: "))
desconto = float(input("Digite o desconto dado: "))

print(f'O valor com desconto aplicado é R${preco - (preco * (desconto / 100))}')