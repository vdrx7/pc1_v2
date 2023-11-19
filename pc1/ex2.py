consumo = float(input('Cuanto fue su consumo?: '))
porcen = float(input('Que porcentaje de propina desea dejar?: '))
propina = consumo*(porcen/100)
print(f'La propina que debe dejar es de ${propina:.2f}')
