age = 12

def admission_cost (age):
    if age < 4:
        price = 0
    elif age < 18:
        price = 25
    elif age < 65:
        price = 40
    else:
        price = 20
    print(f"Your admission cost is ${price}")
admission_cost(age)
admission_cost(19)
admission_cost(3)
admission_cost(67)