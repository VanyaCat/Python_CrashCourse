#2-3 Personal Message
#var = "Seth"
#message = f"Hello, {var} would you like to learn some Python today?"
#print(message)

#2-4 Name Cases
first_name = "Seth"
last_name = "Lilavivat"

#print(first_name.lower(), last_name.lower())

full_name = f"{first_name} {last_name}"
print(full_name, "\n")
print(full_name.lower())

# What other ways can we print the same string?

# https://docs.python.org/3/library/string.html
print(first_name + ' ' + last_name)
print(first_name, last_name)
print('{} {}'.format(first_name, last_name))
print('{0} {1}'.format(first_name, last_name))

# What other ways can we print a string?

#2-5 Famous Quote

message = "Albert Einstein once said, \"A person who never made a mistake never tried anything new.\""
print(message, "\n")

#2-6

famous_person = "Albert Einstein"
new_message = f"{famous_person} once said, \"A person who never made a mistake never tried anything new.\""
print(new_message, "\n")

#2-7 Striping

name_tab = "Seth\t"
name_newline = "Seth\n"
print(name_tab.strip(), name_tab, "\n")
print(name_newline.strip(), name_newline)

