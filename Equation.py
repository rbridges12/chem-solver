import Compound

class Equation:
	def __init__(self, equationStr):
		self.equationStr = equationStr
		self.parseEquationStr()

	def parseEquationStr(self):
		sides = self.equationStr.split('=') 
		#divide into 2 sides of reaction
		reactantStrings = sides[0].rstrip().split('+') 
		#divide reactants into compounds, also remove last char which is an unnecessary space
		productStrings = sides[1].lstrip().split('+')
		#same thing for products except remove first char

		self.reactants = []
		#empty list to store compound objects for reactants
		for r in reactantStrings:
			termParts = r.strip().split(' ')
			#split reactant into cf and form and remove extra spaces
			coefficient = int(termParts[0])
			#var for cf as an int
			formula = termParts[1]
			#var for formula
			self.reactants.append(Compound.Compound(coefficient, formula))
			#create a new compound using those vars and add it to reactants list
		self.reactantNum = len(self.reactants)

		self.products = []
		#empty list to store compound objects for reactants
		for p in productStrings:
			termParts = p.strip().split(' ')
			#split product into cf and form and remove extra spaces
			coefficient = int(termParts[0])
			#var for cf as an int
			formula = termParts[1]
			#var for formula
			self.products.append(Compound.Compound(coefficient, formula))
			#create a new compound using those vars and add it to products list
		self.productNum = len(self.products)

	def setCompMass(self, side, index, mass):
		#set the mass of one compound, specifying products or reactants (side), index in that list, and mass to be assigned
		if side == 'Reactants':
			self.reactants[index].setMass(mass)
		elif side == 'Products':
			self.products[index].setMass(mass)

	def getReactant(self, index):
		return self.reactants[index]
		#return the specified reactant

	def getProduct(self, index):
		return self.products[index]
		#return the specified product	