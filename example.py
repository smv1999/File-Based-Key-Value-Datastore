from datastore import *

ds = DataStore()

ds.create('chennai', 'Marina', 120)

print(ds.read('chennai'))