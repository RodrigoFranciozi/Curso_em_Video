peso = float(input("Qual é o seu Peso (Kg)? "))
altura = float(input('Qual é a sua Altura (m)? (Utilize o separador ".")'))

imc = peso / (altura**2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))

if imc < 18.5:
    print("Você está abaixo do peso normal")
elif imc <= 25:
    print("PARABÉNS, você se encontra na faixa de peso normal")
elif imc <= 30:
    print("Você está na faixa de Sobrepeso")
elif imc <= 40:
    print("Você está na faixa de Obesidade")
elif imc > 40:
    print("Você está na faixa de obesidade Morbida. Cuidado!")    