class Vehicle:
	def __init__(self, fuelType, maxPassangers):
		self.fuelType = fuelType
		self.maxPassangers = maxPassangers

	def Move():
		print("It's moving!")

	def setFuelType(self, fuelType):
		self.fuelType = fuelType

	def setMaxPassangers(self, maxPassangers):
		self.maxPassangers = maxPassangers

	def getFuelType(self):
		return self.fuelType

	def getMaxPassangers(self):
		return self.maxPassangers

class Ship(Vehicle):
	def __init__(self, fuelType, maxPassangers, age, typ, countryOfManufacture):
		super().__init__(fuelType, maxPassangers)
		self.age = age
		self.typ = typ
		self.countryOfManufacture = countryOfManufacture

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
	def __init__(self, fuelType, maxPassangers, age, typ, wingsLength):
		super().__init__(fuelType, maxPassangers)
		self.age = age
		self.typ = typ
		self.wingsLength = wingsLength

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

