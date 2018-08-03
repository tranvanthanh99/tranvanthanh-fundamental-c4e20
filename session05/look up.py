teencode ={
    "hc": "học",
    "ng": "người",
    "pt": "phát triển,phương trình, phân tích",
    "eny": "em người yêu",
    "any": "anh người yêu",
    "ns": "nói",
    "ngta": "người ta",
    "lm": "làm",
    "r": "rồi",
    "stt": "status"
}
loop = True

while loop:

    
    for key in teencode.keys():
        print(key, end="\t")
    print()    
    ycode = input("your code? ")
    if ycode  in teencode:
        print("translation: ",teencode[ycode])
    else:
        print("* "*50)
        ask = input("not found, do you want to contribute this word (Y/N)? ").upper()
        if ask == "Y":
            trans = input("Enter your translation: ")
            teencode[ycode]= trans
            print("updated")
        else:
            loop = False  
    print("* "*50)          

    
