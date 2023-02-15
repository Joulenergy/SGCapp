from datetime import datetime
from models import Product
import sys
import json
import ast

# e.g. one column is to type DATE  so it creates today's date:
today = datetime.today().strftime('%Y-%m-%d')

# instantiate the class
db = Product()

# we have 6 columns in the table and need 6 matching bits of data:
'''
date DATE,
sno REAL,
team TEXT
won REAL,
draw REAL,
lost REAL,
team_won REAL,
team_draw REAL,
team_lost REAL'''




item = (today,1,"Ur mum",4,2,6,3,7,8)

# insert the data above into the table using the class method we called i
# inserting the same data 
# normally the thing above and below is to be put into the page used to inupt the data

db.insert(item)

# read all the data in the db back, and loop over the rows
stuff = [][]
count = 0
for item in db.read():
	stuff[count].append(item)
	if len(stuff[count]) == 9:
		def stuff[0]
		count = count + 1
		
input = ast.literal_eval(sys.argv[1])
output = input
output.append(stuff)
print(json.dumps(output))

sys.std.flush()
