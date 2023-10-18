
motorcycles = ["honda", "yamaha", "suzuki"]
print (motorcycles)

motorcycles[0] = "ducati"
print(motorcycles)

motorcycles.append("ducati")
print(motorcycles)

motorcycles.insert(0,"harley")
print(motorcycles)

del motorcycles[0]
del motorcycles[1]
print(motorcycles)

popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

motorcycles = ["honda", "yamaha", "suzuki"]

motorcycles.remove("suzuki")
print(motorcycles)

