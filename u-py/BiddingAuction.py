from replit import clear
def check_winner(biddingrecord):
    highest_bid=0
    for name in biddingrecord:
        bid_amount=biddingrecord[name]
        if bid_amount > highest_bid:
            winner_name=name
            highest_bid=bid_amount
    print(f"The winner is {winner_name} with the bid of {highest_bid}")


bids={}
bidding_end = False


while not bidding_end:
    name= input("Enter your name")
    price = int(input("Enter bid price"))
    bids[name]=price
    should_cont= input("Is there any other bidder? type yes or no.")
    if should_cont=="no":
        bidding_end=True
    elif should_cont=="yes":
        clear()

check_winner(bids)
