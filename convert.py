import conversions

def str_works(currentUnit, desiredUnit):
	# Checks to see if micro is in either str
	cUnit = currentUnit.find('micro')
	dUnit = desiredUnit.find('micro')

	# Checks to see if cUnit is micro or in the conversionTable
	if cUnit == -1:
		cUnit = currentUnit.strip()[-1] in conversions.metricConversions
	else:
		cUnit = True

	# Checks to see if dUnit is micro or in the conversionTable
	if dUnit == -1:
		dUnit = desiredUnit.strip() in conversions.metricConversions
	else:
		dUnit = True

	# If both are True, return true. Else return False!
	if cUnit and dUnit:
		return True
	else:
		return False

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

	conversion1 = conversions.metricConversions[currentUnit]
	conversion2 = conversions.metricConversions[desiredUnit]

	# If current unit isnt base, will multiply nbr to get it in base
	if currentUnit != 'b':
		nbr *= conversion1
		if desiredUnit == 'b':
			print('\n===================\n')
			print(round(nbr, 4), desiredUnit)
			return
	nbr /= conversion2
	print('\n===================\n')
	print (round(nbr, 4), desiredUnit)
