rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random
#####################################
your_choice=int(input("Enter 0 for Rock ,1 for Paper or 2 for Scissors"))
computer_choice=random.randint(0,2)
gameimage=[rock, paper, scissors]
print("Your Choice\n",gameimage[your_choice])
print("Computer Choice\n",gameimage[computer_choice])

if your_choice == computer_choice:
     print("Draw")
elif your_choice==0 and computer_choice==1:
    print("computer win")
elif your_choice==0 and computer_choice==2:
    print("You win")
elif your_choice==1 and computer_choice==2:
    print("computer win")
elif your_choice==1 and computer_choice==0:
    print("You win")
elif your_choice==2 and computer_choice==0:
    print("computer win")
elif your_choice==2 and computer_choice==1:
    print("You win")
elif your_choice >=3:
    print("You lose because of invalid input")