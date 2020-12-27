import time
import json

MAX_DATA_SIZE = 1000000000
MAX_VAL_SIZE = 16384


class DataStore:
    def __init__(self):
        self.datastore = {}
    # Create operation
    # Use syntax : datastore_obj.create(key, value, time_to_live) where time_to_live is optional and is in seconds

    def create(self, key, value, time_to_live=0):
        if key in self.datastore:
            print('error: This key already exists.')
        else:
            if len(self.datastore) < MAX_DATA_SIZE and len(value) < MAX_VAL_SIZE:
                if time_to_live == 0:
                    data = {'value': value, 'time_to_live': time_to_live}
                else:
                    data = {'value': value,
                            'time_to_live':  time.time() + time_to_live}
                if len(key) <= 32:
                    self.datastore[key] = data
                else:
                    print('The keys must be 32 characters in length')
            else:
                print('error: Memory limit exceeded')

    # Read operation
    # Use syntax : datastore_obj.read(key)
    def read(self, key):
        if key not in self.datastore:
            print('error: Given key does not exist in datastore')
            return
        else:
            data = self.datastore[key]
            if data['time_to_live'] != 0:
                if time.time() < data['time_to_live']:
                    return json.dumps({key: data['value']})
                else:
                    print('error: Time of ' + key + ' has expired')
                    return
            else:
                data = self.datastore[key]
                return json.dumps({key: data['value']})

    # Delete operation
    # Use syntax : datastore_obj.delete(key)
    def delete(self, key):
        if key not in self.datastore:
            print('error: Given key does not exist in datastore')
        else:
            data = self.datastore[key]
            if data['time_to_live'] != 0:
                if time.time() < data['time_to_live']:
                    del self.datastore[key]
                    print('Success : The record with key ' +
                          key + ' is successfully deleted.')
                else:
                    print('error: Time of ' + key + ' has expired')
            else:
                del self.datastore[key]
                print('Success : The record with key ' +
                      key + ' is successfully deleted.')

    # Additional Update / Modify operation within its expiry time
    # Use syntax : datastore_obj.update(key, value)
    def update(self, key, value):
        if key not in self.datastore:
            print('error: Given key does not exist in datastore')
        else:
            data = self.datastore[key]
            if data['time_to_live'] != 0:
                if time.time() < data['time_to_live']:
                    self.datastore[key]['value'] = value
                    print('Success : The record with key ' +
                          key + ' is successfully updated.')
                    # After updation, read() is called to display the updated value
                    self.read(key)
                else:
                    print('error: Time of ' + key +
                          ' has expired. So, modify operation cannot be performed.')
            else:
                self.datastore[key]['value'] = value
                print('Success : The record with key ' +
                      key + ' is successfully updated.')
                # After updation, read() is called to display the updated value
                self.read(key)
