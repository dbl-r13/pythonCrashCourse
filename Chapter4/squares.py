# Creating list of numbers with for and range()
squares = []
for num in range(1,11):
    # square = num **2 - Commented this out to refactor code. 
    squares.append(num**2)

# List comprehension way of creating a list. 
squares2 = [val**2 for val in range(5,105,5)]
print(squares2)

print(squares)

digits = [num for num in range(0,10)]

print(digits)
print(f"{min(digits)} is the minimum number of the digits list.")
print(f"{max(digits)} is the maxmum number of the digits list.")
print(f"{sum(digits)} is the sum of all the numbers in the digits list.")

print("\n","="*16, "TRY THIS YOURSELF", "="*16, "\n")
# Count to twenty
for num in range(1,21):
    print(num)

# Count to 1 Milli 
for num in range(0,1_000_001):
    print(num)


# Summing 1 Milli 
print(sum([num for num in range(1,1_000_000)])) #Answer is: 499999500000

# Create list of all Odd Numbers
odd_numbers = [num for num in range(1,21,2)]
print(odd_numbers)

# Print numbers by 3's
for num in range(3,33,3):
    print(num)

# Make list of cubes from numbers 1-10
cubes = []
for val in range(1,11):
    cubes.append(val**3)
print(cubes)

# Use List Comprehension to generate the first 10 cubes
print([num**3 for num in range(1,11)])