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
while len(guest_list) > 2:
    guest_list.pop()
print("The new guest list is: ", ', '.join(guest_list))

#3-8
