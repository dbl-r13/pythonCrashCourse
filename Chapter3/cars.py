cars = ["bmw","audi","toyota","subaru"]
print(cars)

cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

cars = ["bmw","audi","toyota","subaru"]
print("Here is the original list of cars\n",cars)
print("Here is the sorted list of cars\n",sorted(cars))
print("Here is the sorted and reversed list of cars\n",sorted(cars,reverse=True))
print("Here is the original list of cars again\n",cars)

print(f"The length of list cars is: {len(cars)} elements long")