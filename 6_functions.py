
def greeting_functions(name, age):
    print('Welcome', name, 'you are', age, 'years old')

greeting_functions(name = 'Muzammil', age = 24)



def record_user_data(*name):
    print('Welcome '+ str(name[0]))

record_user_data('Tim', 'John', 'Tom')


def my_function():
    return 5+4

a = my_function()
print(a)

