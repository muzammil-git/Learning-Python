# List Methods -> append, remove, insert, extend, copy, pop, reverse, clear, del

countries = ['Japan', "Pakistan", "Maldives", "Bali"] #Business Rules and naming conventions -> Generic 

print(countries[2])
# Range start is inclusive, Range end is exclusive
print("Range", countries[1:3])
print(type(countries))

print("Before", countries)
countries[1] = "Indonesia"

print("After", countries)


numbers = [1,2,3]
fruits = ["Apple", "Banana", "Oranges"]

numbers.extend(fruits)


fruit_numbers = [*numbers, *fruits]
print(fruit_numbers)

winners = ["Muzammil", "Saad", "Monkey"]
winners.append("Areesha")
winners.remove("Monkey")

print("Winners: ", winners)

winners.insert(1, "Reesh")
print("Winners: ", winners)

print(winners.index('Reesh'))

winners.reverse()
print("Winners: ", winners)

winners.pop()
print("Winners: ", winners)

winners.pop(2)
print("Winners: ", winners)


winners_copy = winners.copy()
print(winners_copy)
winners_copy.clear()
print(winners_copy)



del winners
print("Winners: ", winners)

