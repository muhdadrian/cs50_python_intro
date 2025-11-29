import random

coin = random.choice(["heads", "tails"])

print(coin)

"""
@ import random will technically import everything in the module,
not only random.choice

@ the downsize we have to use random.choice -- longer, ugly and annoying
"""
