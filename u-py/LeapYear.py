


year =  int(input("Enter The Year"))
if year % 4 == 0:
    if year % 100 ==0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not a leap year")
    else:
        print("leap year")
else:
    print("not a leap year ")

    
    #    NO             start           YES

    #                  div by 4
    #    not leap                       div by 100
    #                             leap               div by 400
    #                                        not leap             leap