payasos = int(input('Cuantos payasos se vendieron?: '))
munecas = int(input('Cuantas muñecas se vendieron?: '))
pp = 112
pm = 75
peso = (payasos*pp + munecas*pm)/1000
print(f'El peso total del paquete será {peso:.2f}kg')
