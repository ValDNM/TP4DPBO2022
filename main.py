from Vehicle import *
from Person import *


#Dummy Datas
ship_1 = Ship('Marine Gas Oil', 30, 57, 'Cargo Ship', 'Netherlands')
ship_2 = Ship('Marine Gas Oil', 210, 10, 'Aircraft Carriers', 'United State of America')
ship_3 = Ship('Marine Diesel Oil', 20, 15, 'Military Frigate', 'France')
ship_4 = Ship('Marine Diesel Oil', 30, 12, 'Military Destroyer', 'Russian Federation')
ship_5 = Ship('Marine Gas Oil', 120, 20, 'Military Battleship', 'United Kingdom')

airplane_1 = Airplane('Jet A-1', 310, 10, 'Commercial Airbus', 30)
airplane_2 = Airplane('JP-8', 280, 4, 'Commercial Airbus', 29)
airplane_3 = Airplane('Jet A', 305, 14, 'Commercial Airbus', 29)
airplane_4 = Airplane('Jet A-1', 332, 10, 'Commercial Airbus', 32)
airplane_5 = Airplane('JP-5', 260, 12, 'Commercial Airbus', 28)

worker_1 = Job('765927838', 'Albert Sunarto', 'Male', '534283', 'Tokopee', 'Janitor')
worker_2 = Job('394167583', 'Jamal Ahmeebad', 'Male', '387859', 'GoGrab', 'Director')
worker_3 = Job('803291039', 'Joseph Joycee', 'Male', '398409', 'SpeedCar Foundation', 'Pilot')
worker_4 = Job('74167583', 'Krishaa Vareez', 'Female', '686661', 'Vizima Company Ltd', 'Regional Manager')
worker_5 = Job('32511039', 'Phoebe Shelby', 'Female', '938509', 'Shelby Company Ltd', 'Booker')

driver_1 = Driver('78325693', 'Kashmeer Nezjan', 'Male', '000371983', '01-12-2029', 'Truck')
driver_2 = Driver('93827598', 'Kovira Romanova', 'Female', '000341841', '09-01-2045', 'Car')
driver_3 = Driver('89378181', 'Jeremy Jinton', 'Male', '000543289', '02-01-2025', 'Car')
driver_4 = Driver('98927813', 'Amita Kunesh', 'Female', '000341841', '01-01-2031', 'Motorcycle')
driver_5 = Driver('42437598', 'Volodymir Petroshenko', 'Male', '000341841', '12-02-2027', 'Wagon')


#Outputs
print(f'Fuel Type       : {ship_1.getFuelType()}')
print(f'Max Passangers  : {ship_1.getMaxPassangers()}')
print(f'Age             : {ship_1.getAge()} years')
print(f'Ship Type       : {ship_1.getType()}')
print(f'Made In         : {ship_1.getCountryOfManufacture()}\n')

print(f'Fuel Type       : {ship_2.getFuelType()}')
print(f'Max Passangers  : {ship_2.getMaxPassangers()}')
print(f'Age             : {ship_2.getAge()} years')
print(f'Ship Type       : {ship_2.getType()}')
print(f'Made In         : {ship_2.getCountryOfManufacture()}\n')

print(f'Fuel Type       : {ship_3.getFuelType()}')
print(f'Max Passangers  : {ship_3.getMaxPassangers()}')
print(f'Age             : {ship_3.getAge()} years')
print(f'Ship Type       : {ship_3.getType()}')
print(f'Made In         : {ship_3.getCountryOfManufacture()}\n')

print(f'Fuel Type       : {ship_4.getFuelType()}')
print(f'Max Passangers  : {ship_4.getMaxPassangers()}')
print(f'Age             : {ship_4.getAge()} years')
print(f'Ship Type       : {ship_4.getType()}')
print(f'Made In         : {ship_4.getCountryOfManufacture()}\n')

print(f'Fuel Type       : {ship_5.getFuelType()}')
print(f'Max Passangers  : {ship_5.getMaxPassangers()}')
print(f'Age             : {ship_5.getAge()} years')
print(f'Ship Type       : {ship_5.getType()}')
print(f'Made In         : {ship_5.getCountryOfManufacture()}\n')

print(f'Fuel Type       : {airplane_1.getFuelType()}')
print(f'Max Passangers  : {airplane_1.getMaxPassangers()}')
print(f'Age             : {airplane_1.getAge()} years')
print(f'Ship Type       : {airplane_1.getType()}')
print(f'Wings Span      : {airplane_1.getWingsLength()} meters\n')

print(f'Fuel Type       : {airplane_2.getFuelType()}')
print(f'Max Passangers  : {airplane_2.getMaxPassangers()}')
print(f'Age             : {airplane_2.getAge()} years')
print(f'Ship Type       : {airplane_2.getType()}')
print(f'Wings Span      : {airplane_2.getWingsLength()} meters\n')

print(f'Fuel Type       : {airplane_3.getFuelType()}')
print(f'Max Passangers  : {airplane_3.getMaxPassangers()}')
print(f'Age             : {airplane_3.getAge()} years')
print(f'Ship Type       : {airplane_3.getType()}')
print(f'Wings Span      : {airplane_3.getWingsLength()} meters\n')

print(f'Fuel Type       : {airplane_4.getFuelType()}')
print(f'Max Passangers  : {airplane_4.getMaxPassangers()}')
print(f'Age             : {airplane_4.getAge()} years')
print(f'Ship Type       : {airplane_4.getType()}')
print(f'Wings Span      : {airplane_4.getWingsLength()} meters\n')

print(f'Fuel Type       : {airplane_5.getFuelType()}')
print(f'Max Passangers  : {airplane_5.getMaxPassangers()}')
print(f'Age             : {airplane_5.getAge()} years')
print(f'Ship Type       : {airplane_5.getType()}')
print(f'Wings Span      : {airplane_5.getWingsLength()} meters\n')

print(f'NIK        : {worker_1.getNIK()}')
print(f'Name       : {worker_1.getName()}')
print(f'Gender     : {worker_1.getGender()}')
print(f'NIP        : {worker_1.getNIP()}')
print(f'Company    : {worker_1.getCompanyName()}')
print(f'Position   : {worker_1.getPosition()}\n')

print(f'NIK        : {worker_2.getNIK()}')
print(f'Name       : {worker_2.getName()}')
print(f'Gender     : {worker_2.getGender()}')
print(f'NIP        : {worker_2.getNIP()}')
print(f'Company    : {worker_2.getCompanyName()}')
print(f'Position   : {worker_2.getPosition()}\n')

print(f'NIK        : {worker_3.getNIK()}')
print(f'Name       : {worker_3.getName()}')
print(f'Gender     : {worker_3.getGender()}')
print(f'NIP        : {worker_3.getNIP()}')
print(f'Company    : {worker_3.getCompanyName()}')
print(f'Position   : {worker_3.getPosition()}\n')

print(f'NIK        : {worker_4.getNIK()}')
print(f'Name       : {worker_4.getName()}')
print(f'Gender     : {worker_4.getGender()}')
print(f'NIP        : {worker_4.getNIP()}')
print(f'Company    : {worker_4.getCompanyName()}')
print(f'Position   : {worker_4.getPosition()}\n')

print(f'NIK        : {worker_5.getNIK()}')
print(f'Name       : {worker_5.getName()}')
print(f'Gender     : {worker_5.getGender()}')
print(f'NIP        : {worker_5.getNIP()}')
print(f'Company    : {worker_5.getCompanyName()}')
print(f'Position   : {worker_5.getPosition()}\n')


