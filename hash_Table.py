# IDENTIFICATION - Name: Elley Folks, Student ID: 010139574 

class hash_Table:
    '''
    Class that manages a hash table, uses chaining to handle collisions.

    Contains methods to insert, update, and search for items from the hash table.
    '''
    
    def __init__(self, length:int = 40):
        '''
        Initializes a new instance of the hash table class with the specified length.

        Args:
            length (int, optional): The initial length of the hash table. Defaults to 40.

        Returns:
            None

        Raises:
            ValueError: If the provided length is not a positive integer.
        '''

        # checks if valid integer was passed in params
        if not isinstance(length, int) or length <= 0:
            raise ValueError("Length of hash table must be a positive integer.")
        
        else:
            # creates hash table with specified length / size
            self.length = length
            self.hash_array = [[] for _ in range(self.length)]


    def insert_item(self, key, value):
        '''
        Inserts a new (key, value), or if key exists in hash bucket, will update value. Returns true if successful.
        '''
        
        bucket = self.get_hash_bucket(key)

        # updates value if (key, value) already present
        for key_value in enumerate(bucket):
            
            if key_value[0] == key:
                key_value[1] = value
                return True
        
        # CHAINING - if (key, value) not already present, appends to end of list in bucket.
        new_key_value = [key, value]
        bucket.append(new_key_value)
        return True
    

    def search_item(self, key):
        '''
        Searches for value matching a given key in a bucket. Returns value if found, else None.

         Args:
            key: The key to search for in the hash table. Will accept package ID. 

        Returns:
            The value associated with the given key if found, otherwise returns None.
        '''
        
        bucket = self.get_hash_bucket(key)

        for key_value in bucket:
            
            if key_value[0] == key:
                return key_value[1]
            
        print(f"ERROR Key:Value pair for searched {key} not found.")
        return None
    

    # Retrieves the specific bucket list at the hash index.
    def get_hash_bucket(self, key):
        hash_index = hash(key) % self.length
        hash_bucket = self.hash_array[hash_index]
        return hash_bucket