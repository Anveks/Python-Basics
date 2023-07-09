import os
print('This is the highest bidder app.')

bidders = []

def check_highest(bidders):
    highest_bid = 0
    highest_bidder = ''

    for bidder in bidders:
        if bidder['bid'] > highest_bid:
            highest_bid = bidder['bid']
            highest_bidder = bidder['name']

    print(f'The highest bid is $ {highest_bid} made by {highest_bidder}! 🎉')    

def get_user_data():
    name = input('Type your name: \n')
    bid = input('Set your bid: \n')
    bidders.append({'name': name, 'bid': int(bid)})
    add_another = input('Is there anyone else who wants to make a bid? Type yes or no. \n').lower()

    if add_another == 'yes': 
        os.system('cls')
        get_user_data()
    else: check_highest(bidders) 

get_user_data()

           