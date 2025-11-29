def total(galleons, sickels, knuts):
    return(galleons * 17 + sickels) * 29 + knuts

coins = [100, 50, 25]

print(total(coins[0], coins[1], coins[2]), "Knuts")
