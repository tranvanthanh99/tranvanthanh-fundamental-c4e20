prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

for key,value in prices.items():
    print(key)
    print("Price: ",value)
    print("stock: ",stock[key])
    print()

total = 0
for key,value in prices.items():
    total += value*stock[key]

print("total = ",total)