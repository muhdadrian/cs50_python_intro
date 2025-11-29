def total(galleons, sickels, knuts):
    return(galleons * 17 + sickels) * 29 + knuts

coins = [100, 50, 25]

print(total(*coins), "Knuts")


# *coins will unpack the list of coins.