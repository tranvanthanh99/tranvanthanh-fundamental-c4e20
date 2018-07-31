num=int(input("Enter a number: "))
is_prime=True

i=2

while i<num:
    if num %i ==0:
        is_prime=False
    i+=1    

    
if is_prime :
    print("{} is a prime number".format(num))
else:
    print("{} is not a prime number".format(num))    



    