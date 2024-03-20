a = int(input("digite primeiro o numero: "))
b = int(input('digite o segundo numero: '))
c = int(input('diigte terceiro numero: '))
menor = b
if a<b and a<c:
    menor = a
if c<a and c<b:
    menor =  c
print('o menor numero digitado foi {}'.format(menor))

# verificando se menor 
#  se verificar maior nao muda muita coisa somente o uso de > 
# mesmo esquema 
maior = b 
if a>b and a>c:
    maior = a
if c>a and c>b:
    maior = c
    print('o maior numero digitado foi {}'.format(maior))
        