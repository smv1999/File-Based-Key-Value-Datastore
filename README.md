# File Based Key Value Datastore

This is a File Based Key-Value Datastore that supports basic CRUD (Create, Read, Update, Delete) operations developed using ```Python```.

The data store will support the following functional requirements:

1. It can be initialized using an optional file path. If one is not provided, it will reliably create itself in a reasonable location on the laptop
1. A new key-value pair can be added to the data store using the Create operation. The key is always a string - capped at 32chars. The value is always a JSON object-capped at
16KB.
1. If Create is invoked for an existing key, an appropriate error must be returned. 4. A Read operation on a key can be performed by providing the key, and receiving the
value in response, as a JSON object.
1. A Delete operation can be performed by providing the key.
1. Every key supports setting a Time-To-Live property when it is created. This property is optional. If provided, it will be evaluated as an integer defining the number of seconds
the key must be retained in the data store. Once the Time-To-Live for a key has expired, the key will no longer be available for Read or Delete operations,
1. Appropriate error responses must always be returned to a client if it uses the data store in unexpected ways or breaches any limits.

The data store will also support the following non-functional requirements:

1. The size of the file storing data must never exceed 1GB.
1. More than one client process cannot be allowed to use the same file as a data store at any given time 
1. A client process is allowed to access the data store using multiple threads, if it desires to The data store must therefore be thread-safe.
1. The client will bear as little memory costs as possible to use this data store, while deriving maximum performance with respect to response times for accessing the data store.
