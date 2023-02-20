from sys import flags


def prime_checker(number):
    flag= True
    for i in range (2 , number-1):
        if number % i == 0:
           flag = False

           
    if flag == True:
        print("prime")
    else :
        print("not prime")
    
            


n= int(input("Check this number:"))
prime_checker(number=n)