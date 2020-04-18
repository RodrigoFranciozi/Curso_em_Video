def fatorial(n, show=False):
    
    """
    -> Calcula o fatorial de um numero.
    :param n: O número  a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do fatorial de um número n.
    """
    f = 1
    for c in range(n, 0 ,-1): #começa do número, conta até o zero, voltando de 1 em 1.
        if show:
            print (c, end='')
            if c > 1:
                print (' X ', end = '')
            else:
                print(' = ', end ='')
        f *=c
    return f

help(fatorial)
print(fatorial(5))