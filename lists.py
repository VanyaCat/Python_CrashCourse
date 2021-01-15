#lists


#3-4
guest_list = ['Jonfen', 'Momma', 'Sox']


#why when I uncomment out lines 9 - 13 it doesn't work. It changes the list to a str
#message = "you are invited to dinner!"


#for guest_list in guest_list:
#    print("Hi", guest_list, message)

#3-5
old_guest = 'Jonfen'
guest_list.remove(old_guest)
print(old_guest.title(), "can't make it.", "\n")
new_guest = 'Maga'
guest_list.insert(0, new_guest)
print(new_guest.title(), "can make it instead.", "\n")
print("The new guest list is: ", ', '.join(guest_list))