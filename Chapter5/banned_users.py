banned_users = ['andrew', 'Carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()} you can post a response if you wish.")

game_active = True
can_edit = False

car = 'subaru'


print('Is there a Subaru in the list? I predict True')
print(car =='subaru')
print('Is there a Subaru in the list? I predict False') 
print(car =='audi')

print("This is the 10 tests:")
nums = list(range(1,11))
print(nums)

for num in nums:
    print(f"Is {num} even? {num%2==0}")

