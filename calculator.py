# Simple Calculator Program
header= '******Welcome to the World of Calculations!******'
print(header.center(80,))
sil= '--Made by: Zubair'
print(sil.center(120))

while True:
    num1 = input('Enter your First Number:')
    num2 = input('Enter your Second Number:')

    print('Enter A for Addition. \nEnter S for Subtraction. \nEnter M for Multiplication. \nEnter D for Division. \nEnter R for Remainder. \nEnter E for Exponential. \nEnter exit for Exiting the program.')
    operation = input('Enter your Operation:')

    if operation.lower() == 'exit':
        print('Exiting the program. Goodbye!')
        break

    if operation == 'A':
        print('The sum of', num1, 'and', num2, 'is:', int(num1) + int(num2))
    elif operation == 'S':
        print('The difference of', num1, 'and', num2, 'is:', int(num1) - int(num2))
    elif operation == 'M':
        print('The product of', num1, 'and', num2, 'is:', int(num1) * int(num2))
    elif operation == 'D':
        print('The division of', num1, 'and', num2, 'is:', int(num1) / int(num2))
    elif operation == 'R':
        print('The remainder of', num1, 'and', num2, 'is:', int(num1) % int(num2))
    elif operation == 'E':
        print('The exponential of', num1, 'and', num2, 'is:', int(num1) ** int(num2))
    else:
        print('Invalid Operation')

    restart = input('Do you want to perform another calculation? (yes/no): ')
    if restart.lower() != 'yes':
        print('Exiting the program. Goodbye!')
        break

