dict = {
    'name' : 'Muzammil',
    'age' : 24,
    'nationality' : 'U',
    'qualification' : 'BSCS',
    'fav_food' : ["Pizza Fries", "Molten Lava with Ice-cream"],
    'think_fast' : True
}


for key, value in dict.items():
    print('Key: ', key, ' | ', 'Value: ', value)


print('-------x-------')

print("name:", dict["name"])
print("age:", dict["age"])
print("nationality:", dict["nationality"])
print("qualification:", dict["qualification"])
print("Fav Food:", dict["fav_food"]   )

print("Len of Dict:", len(dict))
print('Info:', dict)