class Person:
	#constructor
	def __init__(self, nik, name, gender):
		self.nik = nik
		self.name = name
		self.gender = gender

	def sleep():
		print("Zzzzzzzz")
		
	#set dan get methods
	def setNIK(self, nik):
		self.nik = nik

	def setName(self, name):
		self.nama = name

	def setGender(self, gender):
		self.gender = gender

	def getNIK(self):
		return self.nik

	def getName(self):
		return self.name

	def getGender(self):
		return self.gender

class Job(Person):
	#constructor
	def __init__(self, nik, name, gender, nip, companyName, position):
		#menggunakan super() untuk pass attribute" yang ada pada __init__() setelahnya ke Job
		super().__init__(nik, name, gender)
		self.nip = nip
		self.companyName = companyName
		self.position = position
	
	#set dan get methods
	def setNIP(self, nip):
		self.nip = nip

	def setCompanyName(self, companyName):
		self.companyName = companyName

	def setPosition(self, position):
		self.position = position

	def getNIP(self):
		return self.nip

	def getCompanyName(self):
		return self.companyName

	def getPosition(self):
		return self.position

class Driver(Person):
	#constructor
	def __init__(self, nik, name, gender, lisenceID, activeUntil, vehicleType):
		#menggunakan super() untuk pass attribute" yang ada pada __init__() setelahnya ke Driver
		super().__init__(nik, name, gender)
		self.lisenceID = lisenceID
		self.activeUntil = activeUntil
		self.vehicleType = vehicleType
	
	#set dan get methods
	def setLisenceID(self, lisenceID):
		self.lisenceID = lisenceID

	def setActiveUntil(self, activeUntil):
		self.activeUntil = activeUntil

	def setVehicleType(self, vehicleType):
		self.vehicleType = vehicleType

	def getLisenceID(self):
		return lisenceID

	def getActiveUntil(self):
		return activeUntil

	def getVehicleType(self):
		return vehicleType

