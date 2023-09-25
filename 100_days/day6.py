#Blind auction game

auction=False
bids={}

def highest_bidder(bidding_record):
    highest_bid=0
    winner=""
    for bidder in bidding_record:
        bid_amount=bidding_record[bidder]
        if bid_amount>highest_bid:
            highest_bid=bid_amount
            winner=bidder
    print(f"The winner is {winner} with the {highest_bid} amount")


while not auction:

    name=input("What is your name?: ")
    price=int(input("Whta is your bid?: "))
    bids[name]=price
    reply=input("Are there any bidders? Type Yes or No\n").lower()
    if reply=="no":
        auction=True
        highest_bidder(bids)