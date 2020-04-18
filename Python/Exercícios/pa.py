p = int(input('Primeiro termo:' ))
r = int(input('Razão:' ))
cont = int(input('Quantos números você quer que mostre: '))
termo = p + (cont -1) * r

for c in range(p, termo + r, r):
    print('{}'.format(c), end = ' -> ')
print('FIM')
                            
# range (inicio, parada, passo)  


