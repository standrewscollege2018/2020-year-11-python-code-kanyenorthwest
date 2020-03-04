auction_item = str(input("What is being sold at the auction? "))
keep_asking = True
keep_bidding = False

while keep_asking == True:
    try:
        reserve_price = int(input("What is the reserve price for {}? ".format(auction_item)))
        keep_asking = False
    except:
        print("Please enter a number.")
        print("This is an auction for the {}, reserve price is ${}.".format(auction_item,reserve_price))

keep_bidding = True
while keep_bidding == True:
    bid_name = str(input("What is your name? "))
try:
    bid = int(input("Amount for bidding: "))
except:
    print("Please enter an amount.")
print("{} enters the auction with a bid of ${}.".format(bid_name,bid))

previous_bid = bid

if previous_bid > bid:
    print("The highest bid so far is held by {} with a bid of ${}.".format(bid_name,previous_bid))
else:
    print("The highest bid so far is held by {} with a bid of ${}.".format(bid_name,bid))