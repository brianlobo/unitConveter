import convert

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

	# Grabs users current and desired unit
	currentUnit = input("\nPlease enter what you want converted\n|example: 12 k (km or kg)|\n:")
	desiredUnit = input('\nPlease enter your desired unit\n|example: c (cm or cg)|\n:')
	if desiredUnit == '' or currentUnit == '':
		user_types_nothing()

	# Checks to see if input is valid
	# If valid, will preform conversion
	if convert.str_works(currentUnit, desiredUnit) == True:
		convert.convert(currentUnit, desiredUnit)
	else:
		user_types_error()

if __name__ == '__main__':
	print_abbreve_table()
	main()
