
# -*- coding: utf-8 -*-
import math

def greeting():
    # Use a breakpoint in the code line below to debug your script.
    print('\nWelcome to the Python Calculator!')
    print('\t - Press H for instructions.')
    print('\t - Press Q to exit.\n')

def printhelpGuide():
    print('The following operations are supported for a single operation:')
    print('\t [!, sin, tan, cos, ^]')
    print('\t\t To use !: e.g 5!')
    print('\t\t To use ^: e.g 5 3 ^')
    print('\t\t To use sin: e.g sin 45')
    print('\t\t\t - Same applies with cos and tan operations\n')
    print('The following operations are supported for a two or more operations:')
    print('\t [+, -, *, /]\n')
def factorial(exp):
    try:
        x = int(exp.split('!')[0])  # caso seja fatorial mais de 1 algarismo (e.g 10)
        result = math.factorial(x)
        return result
    except ValueError:
        print('Factorial can only be calculated with positive numbers')

def power(exp):
    substring = exp.split()
    base = float(substring[1]) #base
    exponent = float(substring[2]) #expoente
    result = math.pow(base, exponent)
    return result


def trignometrics(exp):
    result = 0.0
    substring = exp.split() # separar a string em [operador] [numero]
    operator = substring[0] #operador (sin, tan, cos)
    number = float(substring[1]) #numero
    if operator == 'sin':
        result = math.sin(number)
    elif operator == 'cos':
        result = math.cos(number)
    elif operator == 'tan':
        result = math.tan(number)

    return result


def start():
    expression = ''
    compareQuit = 'Q'
    compareHelp = 'H'
    while expression.casefold() != compareQuit.casefold(): #Para que seja case-insensitive
        expression = input('Please enter an expression:\n')
        try:
            if expression.casefold() == compareQuit.casefold():
                print('The calculator will now close.')
                break
            if expression.casefold() == compareHelp.casefold():
                printhelpGuide()
                continue
            elif expression.isalpha():
                print('Not a mathematical expression. Please enter a mathematical expression')
                continue
            elif expression.endswith('!'): 
                answer = factorial(expression)
                print('Result is:', answer)
                continue
            elif expression.startswith('^'): 
                answerP = power(expression)
                print('Result is:', answerP)
                continue
            elif expression.startswith('sin') or expression.startswith('cos') or expression.startswith('tan'):
                ans = trignometrics(expression) 
                print('Result is:', ans)
                continue
            operatorList = ['+', '/', '*', '-']
            for l in operatorList:
                found = expression.find(l)
            if found and expression[-1].isdigit() or expression.endswith(')') or expression.startswith('('):
                evaluated = str(expression)
                print('Result is: ', eval(evaluated)) #não recomendado, mas como apenas é utilizado se expressão conter operador, mitigamos
            else:
                print('Not a mathematical expression. Please enter a mathematical expression')

        except IndexError:
            print('Invalid expression')
        except SyntaxError:
            print("Invalid expression.")
        except NameError:
            print("Invalid expression.")
        except ValueError:
            print("Invalid expression.")


#Correr a calculadora
greeting()
start()
