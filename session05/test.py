# quy = ["Quy",20,"Vinh phuc",2,3,["anime","ping pong"]]
# dictionary
# CRUD
# key : value

person = {
    "name": "Quy",
    "age": 20,
    "university": "hust",
    "ex": 2,
    "favs": ["anime","ping pong"]
}

person["gender"]="male"



# key = "ex"
# if key in person:
#     print(person[key])
# else:
#     print("Not found")    

# for key in person.keys():
#     print(key, end="\t")

# for key, value in person.items():
#     print(key,value)    

# for value in person.values():
#     print(value)

# update
# person["ex"]= 20

# delete
del person["age"]
print(person)
