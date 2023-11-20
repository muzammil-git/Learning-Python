'''
Take 2 inputs
Make function  for +, -, /, *
show result
'''


try:
    num1 = int(input('Enter first number: '))
    num2 = int(input('Enter second number: '))
except:
    print('invalid')


operation = input("What operation do you want to perform: ")

def calculate(a, b):
    match operation:
        case '+':
            result = a+b 
        
        case '-':
            result = a-b 

        case '*':
            result = a*b
        
        case '/':
            result = a/b
        
        case _:
            result = "Invalid Operation"

    return result


statement = calculate(num1, num2)
print("Result: ",statement)


# def add(a, b):
#     return a+b

# def subtract(a, b):
#     return b-a

# def multiply(a, b):
#     return a*b

# def divide(a, b):
#     return b/a





