from time import sleep

def maior(*n):
    count = bigger = 0
    print ('-=' *30) #printa o que esta entre '', o número de vezes que estiver sendo multiplicado
    print('Analisando os valores [...]')
    for value in n:
        print(f'{value}', end = '', flush = True)  
        sleep(0.3)
        if count ==0:
            bigger = value
        else:
            if  value > value:
                bigger = value
        count += 1
    print(f' \n Foram informados {count} números')
    print(f'O maior valor encontrado foi {value}')            

maior(1, 3, 5 ,8)

# Inserindo um * antes de um parâmetro, dito que não sei quantos irei receber e "desempacotarei" esse valores em um estrutura de repetição