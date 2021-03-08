#hw6_1
obj = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b,
    '**': lambda a, b: a ** b,
    'sqrt': lambda a, b: a ** (1/b),
}

def getValidNumber():
    while True:
        number = input('Enter a number: ')
        if number.isdigit():
            return float(number)
        else:
            print('This input is invalid.')

def getOperator():
    while True:
        operator = input('Enter operation +, -, *, /, **, sqrt: ')
        if operator in ['+', '-', '*', '/', '**', 'sqrt']:
            return operator
        else:
            print('This input is invalid.')

def getNumbersAndOperator():
    number1 = getValidNumber()
    operator = getOperator()
    while True:
        number2 = getValidNumber()
        if (operator == '/' or operator == 'sqrt') and number2 == 0:
            print('You cant divide or root, enter another number')
        else:
            break
    return number1, operator, number2

number1, operator, number2 = getNumbersAndOperator()
    
print('Your result: ', obj[operator](number1, number2))

#hw6_2

def halfTriangle():
    num = int(input('Input number: '))
    str_ = ''
    for i in range(1, num + 1):
        if i == num:
            str_ += '*' * i
        else:
            str_ += '*' * i + '\n'
    return str_

print(halfTriangle())

def tree():
    num = int(input('Input number: '))
    str_ = ''
    for i in range(1, num + 1):
        tmpl = ' ' * (num - i) + '*' * (2 *i)
        if i == num:
            str_ += tmpl
        else:
            str_ += tmpl + '\n'
    return str_

print(tree())

#hw6_3

def eratosphen():
    n = int(input('Input number: '))
    numbers = list(range(2, n + 1))
    for i in numbers:
        for j in range(2 * i, n+1, i):
            if j in numbers:
                numbers.remove(j)
    return numbers

print(eratosphen()) 

#hw6_4

def getYear():
    while True:
        number = input('Enter a year: ')
        if number.isdigit():
            return int(number)
        else:
            print('This input is invalid.')

def checkYears():
    year = getYear()
    if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
        return 'This is a usual year!'
    else:
        return 'This is a leap year!'

print(checkYears())
