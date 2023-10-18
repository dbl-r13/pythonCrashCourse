original_list = ["Michael Jordan", "MLK", "Denzel Washington", "The Rock", "Kevin Hart"]

print(original_list)

new_list = []

cannot_make = []


cannot_make.append(original_list.pop())
cannot_make.append(original_list.pop(0))
for guest in original_list:
	new_list.append(guest)

new_list.append("JFK")
new_list.append("Jay-z")

print(original_list) 
print(cannot_make)
print( new_list)

