import random
easy = 10
hard = 5
number = random.randint(1,100)
print("--Welcome to Guess The Number--")
print("I'm thinking the number between 1 to 100")
level = input("Enter Difficulty 'easy' or 'hard' ")

def gameplay(x):
    print(f"You will have {x} Guesses")
    print(number)
    while(x != 0):
        print(f"You have {x}  attempt remaining to guess the number")
        guess_no=int(input("Guess The Number :"))
        if(number == guess_no):
            print("You guessed it correct")
            break
        elif number < guess_no:
            print("Too High")
            x -=1
        elif number > guess_no:
            print("Too Low")
            x -=1
    if x==0:
        print("Game Over. You haven't guess the number")

if level=="easy":
    gameplay(easy)
elif level=="hard":
    gameplay(hard)


