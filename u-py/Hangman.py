
import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word =["ardvark","baboon","camel"]
ch = random.choice(word)
word_length=len(ch)
dash_list=[]
print(word_length)
for i in range (0,len(ch)):
    dash_list.append("_")

letter=""
check=True
no=len(stages)-1
while check:
    if "_" in dash_list:
            letter = input("Guess the letter ")
            for i in range(0,len(ch)):
                 if ch[i] == letter:
                    dash_list[i]=ch[i]
    if letter not in ch:
        no -=1
        if no == 0:
            print("you lose")
                       

    else:
        check=False
         

    print(dash_list)
    if check ==False:
        print("You win")
    
   
