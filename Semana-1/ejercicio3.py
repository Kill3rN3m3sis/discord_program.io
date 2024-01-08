#Create an university enrollment system with the followin Characteristics:

"""
*The system has a login with username and password.
*Upon Logging in, a menu displays the avaliable program: Computer Science, Medicine, Marketing and Arts.
*The user must input their first name, last name and chocen program.
*Each program has only 5 available slots. The system will store the data of each registered user, 
and if it exceeds the limit, it should display a message indicating the program is unavailable.
*If login information is incorrect three times, the system should be locked.
*The user must choose a campus from three cities: London, Manchester, Liverpool.
*In London, there is 1 slot per program; in Manchester, there are 3 slots per program, an in Liverpool,
there is 1 slot per program
*If the user selects a program at a campus that has no available slots, the system should display the 
option to enroll in the program at another campus 
"""
#Variables
username = ''
password = ''
attempt = 3
user_computer = 5

#Listas 
computer_list = []
medicine_list = []
marketing_list =[]
arts_list =[]
london_list = []
manchester_list = []
liverpool_list = []

class Persona:
    def __init__(self,nam,las_n):
        self.nam = nam
        self.las_n = las_n

def Mostrar():
    k = 0
    while k < len(computer_list):
        print(computer_list[k].nam, computer_list[k].las_n)
        k+=1 


while attempt > 0:
    print('Username: admin')
    print('Password: admin')

    username = input('\n\n\nEnter Username: ')
    password = input('Enter Password: ')
    if username == 'admin' and password == 'admin':
        print('\n\n¡¡Granted Access!!')
        break
    attempt = attempt - 1
    print(f'Incorrect User or Password \nRemaining Attempt {attempt}\n\n ')

else:
    print('Program termination for Excedeed Atempts')


while True:
    print('\n\n\t.:Menu:.')
    print('1.-Computer Science')
    print('2.-Medicine')
    print('3.-Marketing')
    print('4.-Arts')
    print('5.-Exit')

    name = str(input('\n\nRegister your name: '))
    last_name = str(input('\nRegister your last name: '))
    option = int(input('\nChoce the program by entering the corresponding number:  '))

    if option == 1: 
        if user_computer > 0:      
            while user_computer > 0:
                name = name
                last_name = last_name
                per = Persona(name, last_name)
                computer_list.append(per)
                break
            user_computer = user_computer - 1
            print(user_computer)
            Mostrar()

        else:
            print('No es posible registrar mas usuarios')
            
  
    if option == 2:
        print('prueba')

    if option == 3:
        print('prueba')

    if option == 4:
        print('prueba')

    if option == 5:
        print('prueba')

    else: 
        print('\n\n*La opción seleccionada no es valida')




