frase = str(input('Digite uma frase:')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]

print('o inverso de {} é {}'.format(junto,inverso))

if inverso == junto:
    print('Essa frase é um palindromo')
else:
    print('Essa frase não é um palindromo')

# strip() --> Remove os espaços em branco na extrema esquerda e direita da frase ou palavra;
# upper() --> Transforma as letras em maiúsculas;
# split() --> Divide a frase em palavras;
# join() --> junta os espaços em branco pelo o que se encontra dentro dos '';