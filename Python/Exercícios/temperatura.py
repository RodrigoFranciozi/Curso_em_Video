c = float(input("Informe a temperatura em Celcius: "))

f = (9*c) / (5+32)
k = c + 273.15

print("O valor da temperatura de {} °C em Farenheight corresponde a {:.2f} °F".format(c,f))
print("O valor da temperatura de {} °C em Kelvin corresponde a {} K".format(c,k))
