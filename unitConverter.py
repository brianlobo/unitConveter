import re

metricConversions = {
				'Y' : (10 ** 24),
				'Z' : (10 ** 21),
				'E' : (10 ** 18),
				'P' : (10 ** 15),
				'T' : (10 ** 12),
				'G' : (10 ** 9),
				'M' : (10 ** 6),
				'k' : (10 ** 3),
				'h' : (10 ** 2),
				'd' : 10,
				'b': 1,
				'd' : (10 ** -1),
				'c' : (10 ** -2),
				'm' : (10 ** -3),
				'micro' : (10 ** -6),
				'n' : (10 ** -9),
				'p' : (10 ** -12),
				'f' : (10 ** -15),
				'a' : (10 ** -18),
				'z' : (10 ** -21),
				'y' : (10 ** -24)
				}

# Returns the number from the current unit
def grabNbr(str):
	# regex that finds any int or float in the str and returns a list
	nbr = (re.findall(r'\d+(?:\.\d+)?', str))
	return float(nbr[0])

def stripStr(currentUnit, desiredUnit):
	nbr = grabNbr(currentUnit)
	if currentUnit.find('micro') == -1:
		currentUnit = currentUnit.strip()[-1]	# Removes whitespace around str and grabs unit
	else:
		currentUnit = 'micro'
	if desiredUnit.find('micro') == -1:
		desiredUnit = desiredUnit.strip()		# Same thing but str should only be a character
	else:
		desiredUnit = 'micro'

	return nbr, currentUnit, desiredUnit

def convert(currentUnit, desiredUnit):
	nbr, currentUnit, desiredUnit = stripStr(currentUnit, desiredUnit)

	conversion1 = metricConversions[currentUnit]
	conversion2 = metricConversions[desiredUnit]

	# If current unit isnt base, will multiply nbr to get it in base
	if currentUnit != 'b':
		nbr *= conversion1
		if desiredUnit == 'b':
			print('\n===================\n')
			print(nbr, desiredUnit)
			return
	nbr /= conversion2
	print('\n===================\n')
	print (nbr, desiredUnit)

# TODO:
def str_works(currentUnit, desiredUnit):
	return True

def print_abbreve_table():
	print ('\nAbbreviations for units:\n|\t(exactly as written)\t|')
	print ('|\tYotta => Y\t\t|\n|\tZetta => Z\t\t|')
	print ('|\tExo => E\t\t|\n|\tPetam => P\t\t|\n|\tTera => T\t\t|')
	print ('|\tGigo => G\t\t|\n|\tMega => M\t\t|\n|\tKilo => K\t\t|')
	print ('|\tHecto => h\t\t|\n|\tDeca => d\t\t|\n|\tBase (m, g) => b\t|')
	print ('|\tMicro => micro\t\t|\n|\tNano=> n\t\t|\n|\tPico => p\t\t|')
	print ('|\tFemto => f\t\t|\n|\tAtto => a\t\t|')
	print ('|\tZepto => z\t\t|\n|\tYocto => y\t\t|')


def user_types_nothing():
	print ('\n------------------------------------------------------------')
	print ('------------------------------------------------------------')
	print ('Please be sure to input your current unit and desired unit')
	print ('------------------------------------------------------------')
	print ('------------------------------------------------------------')
	main()

def user_types_error():
	print ('\n----------------------------------------------')
	print ('----------------------------------------------')
	print ('You have entered an invalid conversion format')
	print ('----------------------------------------------')
	print ('----------------------------------------------')
	main()

def main():
	print_abbreve_table()

	# Grabs users current and desired unit
	currentUnit = input("\nPlease enter what you want converted\n|example: 12 k (km or kg)|\n:")
	desiredUnit = input('\nPlease enter your desired unit\n|example: c (cm or cg)|\n:')
	if desiredUnit == '' or currentUnit == '':
		user_types_nothing()

	# Checks to see if input is valid
	# If valid, will preform conversion
	if str_works(currentUnit, desiredUnit) == True:
		convert(currentUnit, desiredUnit)
	else:
		user_types_error()

if __name__ == '__main__':
#	print_abbreve_table()
	main()
