import art
print(art.logo)
continue_game = True
names_and_bids = {}
max_bid = 0

while continue_game:
    name = input("What is your name?: ")
    bid_value = input("What is your bid?: ")
    names_and_bids[name] = bid_value
    more_bidders = input("Are there any more bidders? y or n: ")

    if more_bidders == "y":
        continue_game = True
    else:
        continue_game = False
        print(names_and_bids)

max_bid = max(names_and_bids.values())

winner_key = [k for k, v in names_and_bids.items() if v == max_bid][0]
print(f"The winner is {winner_key} with a bid of ${max_bid}.")
