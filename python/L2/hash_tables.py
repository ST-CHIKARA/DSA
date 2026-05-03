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
# what this simply means is that when we give python a key it converts it into a hash and give it a hash address(in our case here the index of the list) and when we want to access that key it directly jumps to that hash address


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


MAX_HASH_TABLE_SIZE = 4096 # Its just a variable that stores the value 4096

data_list = [None] * MAX_HASH_TABLE_SIZE # we are making a list that have 4096 indexes with values = None (None * 4096)

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

def get_index(data_list,a_string): # Get_index takes 2 arguments our data_list that we made above and the key (a_string) that we want to store like 'Aakash' for example 
    result = 0 # Counter that holds the total numeric value(unicode) of all the letters in the name (key)

    for a_character in a_string: # for loop to loop over each character of the name(key)
        a_number = ord(a_character) # what this does is that takes our single character (a_character) and uses ord() function to return back its unicode which is a universal code assigned to every character, symbol and emoji in every language
        result += a_number # we take that unicode number and add it to our counter 

    list_index = result % len(data_list) # Here what we are doing is that using modulus operator (%) which is used to get a remainder of the division between the total result of the key we converted to unicode and the len of our data_list which is fixed 4096.
    # We are doing this because the index we are trying to get of the key we gave as the argument must be between 0 and 4095 and we dont accidentally get a index higher than the total length of the list.
    return list_index # we return the index 

print(get_index(data_list, '') == 0) # check if an empty string gives the index == 0 since there are no characters to sum and the default value of the result = 0
print()

print(get_index(data_list, 'Aakash') == 585) # To check if the name Aakash hashes to index 585
print()

print(get_index(data_list, 'Don O Leary')) # To get the index of Don O Leary
print()

key, value = 'Aakash', '7878787878' # Assigning key,value pair

idx = get_index(data_list, key) # running the key we just defined through the function to get its index value
print(idx)
print()

print(data_list[idx] == None) # To check if the spot at the index that we got from above is empty(None)
print()

data_list[idx] = (key, value) # We got to index we got from above and in the empty space we just checked we replace the empty space with the tuple (key,value) pair which will be 'Aakash', '7878787878' at index 585

key, value = data_list[idx] # We are unpacking the tuple we just stored by doing to the index and saving their values in the variables key,value
print(value)
print()

print(data_list[idx] == None) # Now we are checking if the index spot where we added our tuple is empty or not
print()

pairs = [kv[0] for kv in data_list if kv is not None] # Using list comprehension we are trying to get the keys of the data we stored in our list(hash map) wherever it is unless the list is empty. 
# 1. So kv[0] means the first value in the tuple that got added which means the key. # 2. kv is the loop variable that stores the tuple when looping through the data_list
# 3. It returns the key if the list is not empty and if it is, it just returns a empty list as the output  
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
            idx = get_index(self.data_list,key)

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

