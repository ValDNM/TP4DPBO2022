class Vehicle:
	#constructor
	def __init__(self, fuelType, maxPassangers):
		self.fuelType = fuelType
		self.maxPassangers = maxPassangers

	def Move():
		print("It's moving!")
	
	#set dan get methods
	def setFuelType(self, fuelType):
		self.fuelType = fuelType

	def setMaxPassangers(self, maxPassangers):
		self.maxPassangers = maxPassangers

	def getFuelType(self):
		return self.fuelType

	def getMaxPassangers(self):
		return self.maxPassangers

class Ship(Vehicle):
	#constructor
	def __init__(self, fuelType, maxPassangers, age, typ, countryOfManufacture):
		#menggunakan super() untuk pass attribute" yang ada pada __init__() setelahnya ke Ship
		super().__init__(fuelType, maxPassangers)
		self.age = age
		self.typ = typ
		self.countryOfManufacture = countryOfManufacture
	
	#set dan get methods
	def setAge(self, age):
		self.age = age

	def setType(self, typ):
		self.typ = typ

	def setCountryOfManufacture(self, countryOfManufacture):
		self.countryOfManufacture = countryOfManufacture

	def getAge(self):
		return self.age

	def getType(self):
		return self.typ

	def getCountryOfManufacture(self):
		return self.countryOfManufacture


class Airplane(Vehicle):
	#constructor
	def __init__(self, fuelType, maxPassangers, age, typ, wingsLength):
		#menggunakan super() untuk pass attribute" yang ada pada __init__() setelahnya ke Airplane
		super().__init__(fuelType, maxPassangers)
		self.age = age
		self.typ = typ
		self.wingsLength = wingsLength

	#set dan get methods
	def setAge(self, age):
		self.age = age

	def setType(self, typ):
		self.typ = typ

	def setWingsLength(self, wingsLength):
		self.wingsLength = wingsLength

	def getAge(self):
		return self.age

	def getType(self):
		return self.typ

	def getWingsLength(self):
		return self.wingsLength

