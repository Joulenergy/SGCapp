from datetime import datetime
from models import Product

# e.g. one column is to type DATE  so it creates today's date:
today = datetime.today().strftime('%Y-%m-%d')

# instantiate the class
db = Product()

# we have 6 columns in the table and need 6 matching bits of data:
'''
date DATE,
category TEXT,
store TEXT,
name TEXT,
price REAL,
link TEXT'''


# matching date

item = (
	today,
	'T-Shirts',
	'Awesome tshirts',
	'Black Logo Tee',
	'24.99',
	'link')

# insert the data above into the table using the class method we called i
# inserting the same data 
db.insert(item)

# read all the data in the db back, and loop over the rows

for item in db.read():
	print(item)