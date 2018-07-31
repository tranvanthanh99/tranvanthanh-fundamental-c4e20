import random

words=["champion","vodka","dungeon"]

word=random.choice(words)
champ=list(word)
champword=[]
while len(champ) != 0:
    a = random.choice(champ)
    champword.append(a)
    champ.remove(a)

print(*champword)    

ans = input("your guess: ")
if ans == word:
    print("huarra")
else:
    print(":(")    