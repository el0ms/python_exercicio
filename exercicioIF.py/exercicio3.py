#importando bibliotecas do python
from datetime import datetime
#inserindo as datas
data1 = input('Digite a primeira data (formato dd/mm/aaaa): ')
data2 = input('Digite a segunda data (formato dd/mm/aaaa):  ')
# comparando as datas 

data1 = datetime.strptime(data1_str, '%d/%m/%y')
data2 = datetime.strptime(data2_str, '%d/%m/%y')

diferença_dias = abs((data1 -  data2 ).days)

print(f'A diferença em dias entre as datas é: {diferença_dias}')