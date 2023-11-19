n1 = float(input('Introducir primer número: '))
n2 = float(input('Introducir segundo número: '))
suma = n1 + n2
resta = n1 - n2
multi = n1*n2
print(f'Menú:\n1. Suma\n2. Resta\n3. Multiplicación')
opcion = int(input('Introduzca el número de la opción deseada: '))
if opcion == 1 :
    print(f'La suma es {suma:.4f}')
elif opcion == 2 :
    print(f'La resta es {resta:.4f}')
elif opcion == 3 :
    print(f'La multiplicación es {multi:.4f}')
else :
    print('Opción inválida')
