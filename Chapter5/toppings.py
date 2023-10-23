requested_topping = "mushrooms"
# Testing for Inequality
if requested_topping != "anchovies":
    print("Hold the anchovies!")

requested_toppings = ["mushrooms", "green peppers", "extra cheese"]
for toppings in requested_toppings:
    if toppings == "green peppers":
        print(f"Sorry, we are all out of {toppings} ring now.")
    else:
        print(f"Adding {toppings}.")

print("\nFinished making your pizza!")

print("="*16, "TRY IT YOURSELF", "="*16)
print()

alien_color = "green"

def alien_one (color):
    if color == "green":
        print("Player has earned 5 points")
    if color == "red":
        print("Better luck next time")

def alien_two (color):
    if color == "green":
        print("Player has earned 5 points")
    else:
        print("Player has earned 10 points")

def alien_three(color):
    if color == "green":
        print("Player has earned 5 points")
    elif color == "yellow":
        print("Player has earned 10 points")
    else:
        print("Player has earned 15 points")

def stages_of_life(age):
    if age < 2:
        stage = "baby"
    elif age < 4:
        stage = "toddler"
    elif age < 13:
        stage = "kid"
    elif age < 20:
        stage = "teenager"
    elif age < 65:
        stage = "adult"
    else:
        stage = "elder"
    if stage[0] in "aeiou":
        print(f"You are an {stage}!")
    else:
        print(f"You are a {stage}!")

fruits = ["kiwi", "apple", "orange"]
def fav_fruit(fruit_list):
    if "banana" in fruit_list:
        print(f"You really like bananas")
    if "kiwi" in fruit_list:
        print(f"You really like kiwis")
    if "apple" in fruit_list:
        print(f"You really like apples")
    if "lemon" in fruit_list:
        print(f"You really like lemons")
    if "orange" in fruit_list:
        print(f"You really like oranges")
stages_of_life(22)
fav_fruit(fruits)