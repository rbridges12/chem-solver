import Compound

def stoich():
	equation = input('Enter balanced equation (format like 1 A + B2 = C3):\n')
	#get equation string
	sides = equation.split('=') 
	#divide into 2 sides of reaction
	reactantStrings = sides[0].rstrip().split('+') 
	#divide reactants into compounds, also remove last char which is an unnecessary space
	productStrings = sides[1].lstrip().split('+')
	#same thing for products except remove first char

	reactants = []
	#empty list to store compound objects for reactants
	for r in reactantStrings:
		termParts = r.strip().split(' ')
		#split reactant into cf and form and remove extra spaces
		coefficient = int(termParts[0])
		#var for cf as an int
		formula = termParts[1]
		#var for formula
		reactants.append(Compound.Compound(coefficient, formula))
		#create a new compound using those vars and add it to reactants list

	products = []
	#empty list to store compound objects for reactants
	for p in productStrings:
		termParts = p.strip().split(' ')
		#split product into cf and form and remove extra spaces
		coefficient = int(termParts[0])
		#var for cf as an int
		formula = termParts[1]
		#var for formula
		products.append(Compound.Compound(coefficient, formula))
		#create a new compound using those vars and add it to products list

	for i in reactants:
		i.setMass(float(input('Enter mass(g) of ' + i.formula + '\n')))
	#get masses of each reactant
	for i in products:
		i.setMass(float(input('Enter mass(g) of ' + i.formula + '\n')))
	#get masses of each product

	limitCfs = []
	#empty list for limiting coefficients
	for i in reactants:
		limitCfs.append(i.limitCf)
	minCf = min(limitCfs)
	limitingReactant = reactants[limitCfs.index(minCf)]

	print('\nReactants\tCoefficient\tMolar Mass\tMoles')
	for i in reactants:
		print(i.formula + '\t\t' + str(i.cf) + '\t\t' + str(i.molarMass) + '\t\t' +'{:.2f}'.format(i.getMoles()))

	print('\nProducts')
	for i in products:
		print(i.formula + '\t\t' + str(i.cf) + '\t\t' + str(i.molarMass) + '\t\t' + '{:.2f}'.format((i.getMoles())))
	
	print('Limiting Reactant: ' + limitingReactant.formula)

stoich()
# 2 C6H6 + 15 O2 = 12 CO2 + 6 H2O
		
 
	