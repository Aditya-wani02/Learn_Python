import random
from replit import clear
# List of card
card_list=[11,2,3,4,5,6,7,8,9,10,10,10]
computer_cards=[]
player_cards=[]
# funtion for choosing Starting Cards 
def choose_card():
    p_card1=random.choice(card_list)
    p_card2=random.choice(card_list)
    player_cards.append(p_card1)
    player_cards.append(p_card2)
    if p_card1==card_list[0] and p_card2==card_list[0]:
        p_card2=random.randrange(1,10)
    c_card1=random.choice(card_list)
    c_card2=random.choice(card_list)
    computer_cards.append(c_card1)
    computer_cards.append(c_card2)
    if c_card1==card_list[0] and c_card2==card_list[0]:
        c_card2=random.randrange(1,10)
    draw_card_computer()
    print(f"Your cards :{player_cards} , Total ={sum(player_cards)}")
    print(f"Computer First Card :{computer_cards[0]}")
    
def show():
    print(f"Your cards :{player_cards} , Total ={sum(player_cards)}")
    print(f"Computer First Card :{computer_cards[0]}")

def draw_card_computer():
    if sum(computer_cards) < 17:
        while sum(computer_cards) < 17:
            computer_cards.append(random.randrange(1,10))
    else: 
        return
def draw_card_player():
    player_cards.append(random.randint(1,10))
def check_winner():
    print(f"Final Hand of player : {player_cards} , Final total {sum(player_cards)}" )
    print(f"Final Hand of Computer: {computer_cards} , Final total {sum(computer_cards)}" )
    if sum(computer_cards) >=22 and  sum(player_cards) >=22:
        return "Both Went above .Draw"
    elif sum(computer_cards) >= 22:
        return "Computer went over.You win"
    elif sum(player_cards) >= 22:
        return "You went over.Computer win"
    elif sum(computer_cards) > sum(player_cards) and sum(computer_cards) < 22:
        return "Computer Win"
    elif sum(computer_cards) < sum(player_cards) and sum(player_cards) < 22  :
        return "You win"
    elif sum(computer_cards) == sum(player_cards ):
        return "Draw"
# choose_card()
start=input("Do you want to start the game? Press y for YES and n for NO")
if start=="y":
    clear()
    choose_card()
    want_draw=input("Do you want to draw a card ? To Draw press 'y' and For pass press 'n' ")
        
    if want_draw=="y":
        draw_card_player()
        show()
        while want_draw=="y":
            want_draw=input("Do you want to draw a card ? To Draw press 'y' and For pass press 'n' ")
            if want_draw=="y":
                draw_card_player()
                show()
            elif want_draw=="n":
                print(check_winner())
                        # start="n"
    elif want_draw=="n":
        show()
        print(check_winner())
                # start="n"
