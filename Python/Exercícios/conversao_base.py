num = int(input("Digite um numero inteiro: "))

def conv_base(num):
    print('''Escolha uma das bases para conversão:
    [1] Converter para Binário
    [2] Converter para Octal
    [3] Converter para hexadecimal''')

    opt = int(input("Sua opção: "))

    if opt == 1:
        print('{} convertido para Binário é igual a {}:'.format(num, bin(num)))

    elif opt ==2:
        print('{} convertido para Octal é igual a {}:'.format(num,oct(num)))

    elif opt ==3:
        print('{} convertido para Hexadecimal é igual a {}:'.format(num,hex(num)))
    
    else:
        print("Opção inválida")
        return conv_base(num)
        
conv_base(num)