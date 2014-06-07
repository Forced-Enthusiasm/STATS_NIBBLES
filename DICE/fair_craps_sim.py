import numpy as np

#Generates a random sample of dice rolls on an even dice

def fair_dice_sampler(N):

	dice_values = [1,2,3,4,5,6]

	number = float(1)/float(6)

	probability_distribution = [number]*6

	sampler = np.random.choice(dice_values,N, p=probability_distribution)

	return sampler

number_of_games = 6000

sample = fair_dice_sampler(number_of_games)

occurences = []

number_of_occurences = 0

for i in range(1,7):

	for x in sample:
		
		if i == x:

			number_of_occurences+=1

	occurences.append(number_of_occurences)

	number_of_occurences = 0	


print "In " +str(number_of_games)+" rolls of a fair dice, we get:"

for i in range(1,7):

	print str(i)+": " + str(occurences[i-1]) + " occurences"


# Simulating a Come-out roll for a craps game over 1000 games


def fair_craps_simulator(N):

	number_of_wins = 0

	dice_1 = fair_dice_sampler(N)

	dice_2 = fair_dice_sampler(N)

	sum_of_dice = [sum(i) for i in zip(dice_1,dice_2)]

	for x in sum_of_dice:

		if x ==7 or x == 11:

			number_of_wins += 1

	return number_of_wins

print "In 1000 games of craps with 2 fair dice, you should win on the first roll " + str(fair_craps_simulator(1000)) + " times."
