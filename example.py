from datastore import *

ds = DataStore()

# Creation
ds.create('chennai', 'Marina', 120)

# Read
print(ds.read('chennai'))

# Delete
ds.delete('chennai')

# Updation / Modification
ds.create('New Delhi', 'India Gate', 120)

ds.update('New Delhi', 'Daula Kuan')
