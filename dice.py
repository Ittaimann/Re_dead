import random
def roll(die):
	return random.randrange(1,die+1)

def multiRoll(amount,die):
	return [roll(die) for x in range(amount)]



