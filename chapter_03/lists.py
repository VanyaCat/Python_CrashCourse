#lists


#3-4
guest_list = ['Jonfen', 'Momma', 'Sox']


#why when I uncomment out lines 9 - 13 it doesn't work. It changes the list to a str
message = "you are invited to dinner!"


for guest in guest_list:
    print("Hi", guest, message)

#3-5
old_guest = 'Jonfen'
guest_list.remove(old_guest)
print(old_guest.title(), "can't make it.", "\n")
new_guest = 'Maga'
guest_list.insert(0, new_guest)
print(new_guest.title(), "can make it instead.", "\n")
print("The new guest list is: ", ', '.join(guest_list))

#3-6
new_guest = 'Vanya'
guest_list.insert(2, new_guest)
print("The new guest list is: ", ', '.join(guest_list))
new_guest = 'Kiko'
guest_list.append(new_guest)
print("The new guest list is: ", ', '.join(guest_list))

#3-7
print("The max number of guests is 2.")
while len(guest_list) > 2:
    guest_list.pop()

for guest in guest_list:
    print("Hi", guest, message)

del guest_list[0]

del guest_list[0]

print(len(guest_list))

#3-8
bucket_places = ['Prague', 'Amsterdam', 'Sedona', 'Tokyo', 'Marrakesh']
print(bucket_places)

print(sorted(bucket_places))
print(bucket_places)
print(sorted(bucket_places, reverse=True))

bucket_places.reverse()
print(bucket_places)

bucket_places.reverse()
print(bucket_places)

bucket_places.sort()
print(bucket_places)

bucket_places.sort(reverse=True)
print(bucket_places)

#3-9
print("The number of bucket places is: ", len(bucket_places), "\n")

#3-10

fav_cars = ['Mazda MX-5', 'BMW Z4 M Coupe', 'Porsche Cayman GT-4', 'Mini Cooper S', 'Honda Civic Si']
fav_cars.append('Ferrari 355')
fav_cars.insert(3, 'Ariel Nomad')
fav_cars.remove('Ferrari 355')
fav_cars.pop()
fav_cars.append('Honda Civic Si')
print(sorted(fav_cars), "\n")

#4-1
fav_pizza = ['Margherita', 'Cheese', 'Sicilian']
for pizza in fav_pizza:
    print("I like", pizza, "pizza!")
print("\n")


#4-2
animals = ['dog', 'cat', 'goat', 'pig']
for animal in animals:
    print(f"A {animal} would make a great pet!")

print("All of these animals would make a great pet!")