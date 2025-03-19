# Fixed version of the coin collection game

coins = 0  # Define the variable before using it

def collect_coin():
    global coins  # Declare 'coins' as a global variable
    coins += 1
    print(f"Coins collected: {coins}")

collect_coin()  # Now it works correctly
collect_coin()
