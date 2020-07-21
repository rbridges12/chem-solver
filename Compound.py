Elements = {'H': 1.008, 'O': 16.00, 'N': 14.01, 'C':12.01, 'Ce':140.116, 'He':4.002602, 'Na': 22.99, 'K': 39.0983}
#dictionary for element molar masses

class Compound:
	def __init__(self, cf, formula, mass=0.0):
		self.cf = cf
		self.formula = formula
		self.mass = mass
		#set variables
		self.splitFormula()
		#split formula into individual elements
		self.findMolarMass()
		#calculate molar mass

	def splitFormula(self):
		self.formList = []
		#empty list for slices of formula string
		start = 0
		c = 1
		#vars for slicing, start c at 1 so you can access [c-1]
		while c < len(self.formula):
			char = self.formula[c]
			pchar = self.formula[c-1]
			#get the current char and the one before it
			if not (pchar.isdigit() and char.isdigit()) and not (pchar.isupper() and char.islower()):
				#if the 2 chars aren't 2 consecutive nums, and they also aren't an upper case followed by a lower case letter
				self.separate(start, c) 
				start = c
				#slice the string between the 2 chars
			c+=1
			#move to next chars
		self.separate(start, len(self.formula))
		#cut it off at the end

		self.formulaList = []
		#empty list for actual elements and amounts
		for i in range(len(self.formList) - 1):
			#iterate through to the end -1 in order to access i + 1
			t = self.formList[i]
			tn = self.formList[i+1]
			#get the current 'term' and the 'next term'
			if t.isalpha():
				#if the first term is alphanumeric
				if tn.isdigit():
					#if the 2nd term is a num, and is therefore the num of atoms
					self.formulaList.append(t + tn)
					#combine the first term (element symbol) and the last term (number of atoms) and add it to the formula list
				else:
					#if the 2nd term isn't a num. therefore the num of atoms is 1
					self.formulaList.append(t + '1')
					#add '1' to the end then add it to the formula list

		last = self.formList[-1]
		#get the last term of formList because it wasn't reached in the for loop
		if last.isalpha():
			#if it's alphanumeric, and therefore an element symbol
			self.formulaList.append(last + '1')
			#put the num of atoms (1) on the end then add it to the formula list

	def separate(self, start, end):
		self.formList.append(self.formula[start:end])		
		#add the specified section of formula string to formList			

	def findMolarMass(self):
		self.molarMass = 0.0
		# allow molar mass to be added to
		for s in self.formulaList:
			if s[1].isdigit(): 
				eSym = s[:1]
				symLen = 1
				#if the 2nd char in the term is a num, the symbol is 1 letter long
			else:
				eSym = s[:2]
				symLen = 2
				#if the 2nd char in the term is a letter, the symbol is 2 letters long
			eMass = Elements.get(eSym, ' ')
			#find atomic mass by looking it up in the dictionary, second arg makes it return ' ' if the key isn't in the dictionary
			if eMass == ' ':
				print("Error: Element " + eSym + " doesn't exist in dictionary")
				exit()
				#if the element isn't in the dict, print an error and exit the script
			self.molarMass += (eMass * int(s[symLen:]))
			#add atomic mass * the last 2 chars of the term aka num of atoms to molar mass

	def findLimitCf(self):
		self.limitCf = self.moles / self.cf	

	def setMass(self, mass):
		self.mass = mass
		self.moles = self.mass / self.molarMass
		self.findLimitCf()

	def __repr__(self):
		return self.formula
	
	def getFormula(self):
		return self.formula

	def getCf(self):
		return self.cf

	def getFormulaList(self):
		return self.formulaList

	def getMolarMass(self):
		return self.molarMass

	def getMoles(self):
		return self.moles

	def getMass(self):
		return self.mass

	def getLimitCf(self):
		return self.LimitCf
	