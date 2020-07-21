import Compound

class Stoich:
	def __init__(self, equation):
		self.equation = equation
		self.parseEquation()

	def parseEquation(self):
		sides = self.equation.split('=') 
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

	 def findLimiter(self):
		 