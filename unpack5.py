def total(galleons, sickels, knuts):
    return(galleons * 17 + sickels) * 29 + knuts

coins = {"galleons": 100, "sickels": 50, "knuts": 25}

print(total(**coins), "Knuts")

# **coins -- double stars -- to unpack dictionary.