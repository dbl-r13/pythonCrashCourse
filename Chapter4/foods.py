# Copying a List

my_foods = ['pizza','falafel','carrot cake']
friends_foods = my_foods[:]

# This is to verify we have two separate lists
my_foods.append('cannoli')
friends_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friends_foods)

print("\n","="*16,"TRY IT YOURSELF","="*16)

list = [1,2,3,4,5,6,7]
print(f"The first three items in the list are: {list[:3]}")

print(f"Three items from the middle of the list are: {list[2:5]}")

print(f"The last three items in the list are: {list[-3:]}")

pizza_toppings =  ["cheese", "pepperoni", "sausage", "supreme", "bbq chicken"]
friend_pizzas =  pizza_toppings[:]
friend_pizzas.append("bacon")

print(f"My favorite pizzas are: {pizza_toppings}")
print(f"My friend's favorite pizzas are: {friend_pizzas}")
