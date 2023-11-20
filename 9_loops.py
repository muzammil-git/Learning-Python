i = 1

while i < 10 or i == 10:
    print(i)
    i += 1


print('------x------')

letter_list = ['a','b','c','d','e']

for letter in letter_list:
    print(letter)


print("-------x-------")

my_dict = {
    'name' : 'Muzammil',
    'age' : 24,
}

for val in my_dict.items():
    print(val[0], val[1])


print("-------x-------")

for i in range(10):
    print(i)
else:
    print('Finished Looping!!')