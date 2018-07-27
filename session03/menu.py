# list / array

menu= ["Cơm","Cá","Thịt bò","Ghẹ","pizza"]

#update
# print(*menu, sep=", ")
# menu[4]= "Tôm"
# print(*menu, sep=", ")

# print(len(menu))
# menu.append("Ghẹ")
# # print(*menu, sep=", ")
# print(len(menu))

# for i in range(len(menu)):
#     print(menu[i])

for index, item in enumerate(menu):
    print("{}. {}".format(index +1,item))

# for item in menu:
#     print(item)
