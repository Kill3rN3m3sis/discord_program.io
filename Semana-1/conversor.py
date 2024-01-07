#Programa que tiene como finalidad realizar la conversion de divisas


#Diccionario con valor de moneda actual con respecto al dolar
valor_moneda = {
'CLP': 888.67,
'USD': 1,
'ARS': 811.70,
'EUR': 0.91,
'TRY': 29.7497,
'GBP': 0.7886,
}

#Variables para ingresar la moneda y guardar el valor una vez realizada la conversion
origen_moneda = ""
cambio_moneda = ""

#Variables para Ingreso, retiro y saldo disponible
saldo = 50

while True:

    print('\t.:Menú:.')
    print('\n1.- Conversor de Divisas')
    print('2.- Ingresar dinero a la cuenta')
    print('3.- Retirar dinero de la cuenta')
    print('4.- Ver saldo disponible')
    print('5.- Salir')

    opcion = int(input('\nIngrese el número de la opción que desea realizar: '))


    if opcion == 1:
        #Mensaje al usuario de las monedas disponibles para la conversion
        print('\n\n\t.:Conversor de Divisas:.\n\nMonedas disponibles para coversion de divisa: \n')


        for moneda in valor_moneda: #Se imprimen en pantalla las monedas del diccionario para mostrar al usuario
            print(moneda)


        origen_moneda = input('\nEscribe la moneda de origen: ')# Solicita al usuario ingresar la moneda de su pais

        while origen_moneda not in valor_moneda: #Bucle para validar que lo que ingrese el usuario se encuentre en el diccionario
            origen_moneda = input('**La moneda ingresada no se encuentra disponible.** \nVerifique e ingrese la moneda correcta nuevamente: ' )

        cambio_moneda = input('\nEscribe la moneda a la que deseas realizar la conversion: ')# Solicita al usuario ingresar la divisa a la que desea convertir
        print()#Salto de linea
        print()#Salto de linea

        while cambio_moneda not in valor_moneda: #Bucle para validar la divisa que ingrese el usuario se encuentre en el diccionario
            cambio_moneda = input ('\n**La moneda ingresada no se encuentra disponible.** \nVerifique e ingrese la divisa a la que desera convertir: ' )
            print()#Salto de linea

        #Solicitar al usuario ingresar la cantidad a convertir
        cantidad = float(input(f'\nIngresa la cantidad de {origen_moneda}: '))
        valor_origen = valor_moneda[origen_moneda]
        valor_cambio = valor_moneda[cambio_moneda]
        valor_total = (valor_cambio/valor_origen) * cantidad

        print(f'{cantidad:.2f} {origen_moneda} equivale a {valor_total:.2f} {cambio_moneda}')
        print()#Salto de linea
        print()#Salto de linea



    elif opcion == 2:
        ingresar_dinero = float(input('\n\n¿Cuanto dinero desea ingresar?--> $'))  
        saldo += ingresar_dinero
        print(f'Saldo disponible en la cuenta: ${saldo:.2f}')
        print()#Salto de linea
        print()#Salto de linea


    elif opcion == 3:
        retirar = float(input('\n\n¿Cuanto dinero desea retirar?--> $'))
        if retirar > saldo:
            print('\nNo cuentas con los fondos suficientes en tu cuenta para realizar el retiro.')
            print()#Salto de linea
        else:
            saldo -= retirar
            print(f'Saldo disponible en la cuenta: ${saldo:.2f}')
            print()#Salto de linea
            print()#Salto de linea

    elif opcion == 4:
        print(f'\n\nSaldo disponible en la cuenta: ${saldo:.2f}')
        print()#Salto de linea
        print()#Salto de linea

    elif opcion == 5:
        print('\n\n¡Gracias por su prefencia!')
        print()#Salto de linea
        print()#Salto de linea
        break



    else: 
        print('\n\nLa opción seleccionada no es valida')








