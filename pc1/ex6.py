edad = int(input('Cuantos años tienes?: '))
if edad < 4 :
    r = 0
elif 4 <= edad <= 18 :
    r = 5
else :
    r = 10
if r >= 5 :
    print(f'El precio de la entrada es: ${r}')
else :
    print('La entrada es gratis')
