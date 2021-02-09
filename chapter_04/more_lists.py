#4-3 Counting to 20
print(list(range(1,21)))

#4-4 1 to 1M
#list = range(1,1000001)
#for i in list:
#    print(i)

#4-5 Summing a Million
list = range(1,1000001)
print(min(list))
print(max(list))
print(sum(list))

#4-6
odd_list = range(1,21, 2)
for i in odd_list:
    print(i)

#4-7
of_three = range(3,33,3)
for i in of_three:
    print(i)

#4-8
cube_list = []
for i in range(1,11):
    value = i**3
    cube_list.append(value)

print(cube_list)

#4-9 list comprehension
cube_list = [i**3 for i in range(1,11)]
print(cube_list)

#4-10
mtb_dest = ['St George', 'Moab', 'Sedona', 'Bend', 'Asheville']
print("The first three items in the list are: ", mtb_dest[0:3])
print("The first three items in the list are:", ', '.join(mtb_dest[0:3]), ".")
print("The middle three items in the list are:", ', '.join(mtb_dest[1:4]), ".")
print("The last three items in the list are:", ', '.join(mtb_dest[2:5]), ".")

#4-11
fav_pizza = ['Criscitos', 'Buena Forcetta', 'Bronx', 'Papalecco']
friend_pizza = ['Pizza Port', 'Reagents', 'Tribute', 'Urban']

for pizza in fav_pizza:
    print(pizza)

for pizza in friend_pizza:
    print(pizza)

#4-13 Tuples
basic_foods = ('starch', 'meat', 'vegetables', 'fruit', 'dessert')
for food in basic_foods:
    print(food)