#Create a banking system with the following features.

"""
*Users must be able to log in with a username and password
*The initial balance in the bank account is $2000
*The system must allow user to deposit, withdraw, view and transfer money.
*The systems must display a menu for users to perform transaction.
"""



#Variables para Ingreso, retiro y saldo disponible
saldo = 2000
user_trasfer = ''
num_account = int
intentos = 3

while intentos > 0:

    user = (input('Enter your username: '))
    password = (input('Enter your password: '))
    if user == "pochita" and password == "123456":
        print('\n\n\t¡¡Granted Access!!\n\n')
        break
    intentos = intentos -1
    print(f'\n\n*Incorrect User or Password  \nremaining attempts {intentos}\n\n')
else:
    print('Program termination for Exceeded Attempts')    



while True:

    print('\n\n\t.:Menú:.')
    print('\n1.- Deposit to Account')
    print('2.- Whitdraw money from the Account')
    print('3.- View available balance')
    print('4.- Transfer money')
    print('5.- Exit')

    opcion = int(input('\nIngrese el número de la opción que desea realizar: '))

    if opcion == 1:
        ingresar_dinero = float(input('\n\n¿Cuanto dinero desea ingresar?--> $'))  
        saldo += ingresar_dinero
        print(f'Saldo disponible en la cuenta: ${saldo:.2f}')
        print()#Salto de linea
        print()#Salto de linea


    elif opcion == 2:
        retirar = float(input('\n\n¿Cuanto dinero desea retirar?--> $'))
                       
        if retirar > saldo:
            print('\nNo cuentas con los fondos suficientes en tu cuenta para realizar el retiro.')
            print()#Salto de linea

        else:
            saldo -= retirar  
            print('\n=================================================')          
            print(f'Saldo disponible en la cuenta: $ {saldo:.2f}')
            print('=================================================')
            print()#Salto de linea
            print()#Salto de linea


    elif opcion == 3:
        print('\n\n=================================================') 
        print(f'Saldo disponible en la cuenta: ${saldo:.2f}')
        print('=================================================') 
        print()#Salto de linea
        print()#Salto de linea

    elif opcion == 4:
        print("\n\n\tIngrese los datos solicitados")
        print('*El saldo máximo para transferir es de $1,000')
        user_trasfer = input('\nNombre del titular de la cuenta: ')
        num_account = input('\nNumero de cuenta o Clave interbancaria: ')
        tranferir = float(input('\n\n¿Cuál es el monto que desea transferir?--> $'))
                      
        if tranferir > saldo:
            print('\nNo cuentas con los fondos suficientes en tu cuenta para realizar el retiro.')
            print()#Salto de linea
        
        elif tranferir > 1000:
            print('\n\nLa transferencia maxima es $1000, elija otra cantidad')
        
        else:
            saldo -= tranferir   
            print(f'\n\nSe realizo transferencia exitosa a: {user_trasfer}')      
            print(f'Número de cuenta {num_account}') 
            print(f'Monto de la transferencia ${tranferir}')  
            print('\n=================================================')
            print(f'\nSaldo disponible en la cuenta: $ {saldo:.2f}')
            print('=================================================')
            print()#Salto de linea
            print()#Salto de linea
            

    elif opcion == 5:
        print('\n\n¡Gracias por su prefencia!')
        print()#Salto de linea
        print()#Salto de linea
        break

    else: 
        print('\n\n*La opción seleccionada no es valida')
