from collections import Counter,OrderedDict

datas = input("Eneter the data: ").lower()
list_data = datas.split()
str_data = ''.join(list_data)

dict_data = Counter(str_data)

alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

for i in alpha:
    if i in dict_data:
        print(i,dict_data[i])
