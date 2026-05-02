# Hash Tables

# Here we will recreate python dictionaries from scratch using a data structure called hash tables. 
# Dictionaries in Python are used to store key-value pairs. Keys are used to store and retrieve values. For example, here's a dictionary for storing and retrieving phone numbers using people's names

phone_numbers = {
    'Aakash' : '9489484949',
    'Hema' : '9595949494',
    'Siddhant' : '9231325312'
}
print()
print(phone_numbers)
print()

print(phone_numbers['Hema'])
print()

phone_numbers['Viru'] = '8787878787'
print(phone_numbers['Viru'])
print()

for name in phone_numbers:
    print('Name:', name, ', Phone Number:', phone_numbers[name])
print()

# Dictionaries in Python are implemented using Hash Tables. A hash table uses a list/array to store the key-value pairs, and uses a hashing function to determine the index for storing or retrieving the data associated with a given key.
# what this simply means is that when we give python a key it converts it into a hash and give it a hash address and when we want to access that key it directly jumps to that hash address


# Our objective now is to implement a hash table class which supports following operations 
# 1. insert :- insert a new key-value pair
# 2. find :- find the value associated with the key
# 3. update :- update the value associated with the key 
# 4. list :- list all the keys stored in the hash table

class HashTable:
    def insert(self,key,value):
        """insert a new key value pair"""
        pass

    def find(self,key):
        """find the value associated with the key"""
        pass

    def update(self,key,value):
        """change the value associated with the key"""
        pass

    def list_all(self):
        """list all the key"""
        pass


MAX_HASH_TABLE_SIZE = 4096

data_list = [None] * MAX_HASH_TABLE_SIZE

print(len(data_list) == 4096)
print(data_list[99] == None )
print()



# Hashing function

# A hashing function is used to convert strings and other non-numeric data types into numbers, which can then be used as list indices. For instance, if a hashing function converts the string "Aakash" into the number 4, then the key-value pair 'Aakash': '7878787878' will be stored at the position 4 within the data list.

# Here's a simple algorithm for hashing, which can convert strings into numeric list indices.

# 1. Iterate over the string, character by character
# 2. Convert each character to a number using the ord function.
# 3. Add the numbers for each character to obtain the hash for the entire string
# 4. Take the remainder of the result with the size of the data list

def get_index(data_list,a_string):
    result = 0

    for a_character in a_string:
        a_number = ord(a_character)
        result += a_number

    list_index = result % len(data_list)
    return list_index

print(get_index(data_list, '') == 0)
print()

get_index(data_list, 'Aakash') == 585
print()

print(get_index(data_list, 'Don O Leary')) 
print()

key, value = 'Aakash', '7878787878'

idx = get_index(data_list, key)
print(idx)
print()

print(data_list[idx] == None)
print()

data_list[idx] = (key, value)

key, value = data_list[idx]
print(value)
print()

print(data_list[idx] == None)
print()

pairs = [kv[0] for kv in data_list if kv is not None]

print(pairs)
print()



# Basic hash table implementation

class BasicHashTable:
    
    def __init__(self,max_size = MAX_HASH_TABLE_SIZE):
        # Create list with None values
        self.data_list = [None] * max_size

    def insert(self,key,value):
        # Find index 
        idx = get_index(self.data_list,key)

        # Store tuple (key,value)
        self.data_list[idx] = key,value

    def find(self,key):
        # Find index
        idx = get_index(self.data_list,key)

        # Retrieve value
        kv = self.data_list[idx]

        if kv is None:
            return None
        else:
            stored_key,value = kv
            return value
        
    def update(self,key,value):
            # Find index
            idx = get_index(data_list,key)

            # Replace with new value 

            self.data_list[idx] = (key,value)

    def list_all(self):
            # Return all keys 
            return [kv[0] for kv in self.data_list if kv is not None]


table = BasicHashTable()

table.insert('Aakash', '9999999999')
table.insert('Hema', '8888888888')

print(table.find('Aakash'))   
print()
print(table.find('Hema'))     
print()

table.update('Aakash', '7777777777')
print(table.find('Aakash'))   
print()

print(table.list_all())   
print()

