# from Chapter3.cars import list_of_cars
dimensions = (200,50)
print(dimensions)

print("Original Dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400,100)

print("\nModified Dimensions:")
for dimension in dimensions:
    print(dimension)

cars = ["bmw","audi","toyota","subaru"]

for car in cars:
    # Testing for Equality
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

requested_topping = 'mushrooms'
# Testing for Inequality
if requested_topping != 'anchovies':
    print("Hold the anchovies!")

# Testing Numerical Comparisons
magic_answer = 35
if magic_answer != 42:
    print("That is not the correct answer. Please try again!")

# Testing Multiple Conditions
age = 35
print(age >= 21 and age<= 40)

requested_topping = ['mushrooms','onions','pineapple']

print('pepperoni' in requested_topping)
print('ducati' not in cars)