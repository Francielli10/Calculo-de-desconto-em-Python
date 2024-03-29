print(50*'-')
print('CALCULE O SEU DESCONTO!')
print(50*'-')
valor_produto = float(input('Digite o valor do produto:R$ '))
qtd_produto = int(input('Digite quantidade do produto:'))
desconto=0.00

if qtd_produto < 200: #Outra maneira: if qtd_produto <201:
  desconto = 0.00
elif 200 <= qtd_produto <=1000: #Outra maneira: elif qtd_produto >=200 and qtd_produto <=1000:
  desconto = 0.05  #5% = 0.05
elif 1000 <= qtd_produto <=2000: #Outra maneira: elif qtd_produto >=1000 and qtd_produto <=2000:
  desconto = 0.10
else:
  qtd_produto >=2000
  desconto = 0.15

total_sem_desconto = valor_produto * qtd_produto
print('O valor total sem desconto é de: R$ {}'.format(total_sem_desconto)) #Outra maneira: print(f'O valor total sem desconto é de: R${total_sem_desconto}')
total_com_desconto = total_sem_desconto - total_sem_desconto * desconto
print('O valor total com desconto é de: R$ {}'.format(total_com_desconto))
