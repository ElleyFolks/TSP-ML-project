# IDENTIFICATION - Name: Elley Folks, Student ID: 010139574 

# RUBRIC - Section A of rubric, hash table.
class hash_table:
    '''
    Section A of rubric.
    
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

        # PROCESS - Checks if valid integer was passed in params.
        if not isinstance(length, int) or length <= 0:
            raise ValueError("Length of hash table must be a positive integer.")
        
        else:
            # PROCESS - Creates hash table with specified length / size.
            self.length = length
            self.hash_array = [[] for _ in range(self.length)]


    # RUBRIC - Section A of rubric, insertion function.
        # FLOW - Inserts a new (key, value) pair into the hash table, or updates the value if the key already exists.
    def insert_item(self, package_Id, value):
        '''
        Inserts a new (key, value), or if key exists in hash bucket, will update value. Returns true if successful.

        Parameters:
            package_Id (hashable): The key to be inserted or updated.
            value: The value associated with the key.

        Returns:
            bool: True if the insertion or update is successful.
        '''
        
        # PROCESS - Gets the hash bucket of the corresponding key passed in.
        bucket = self.get_hash_bucket(package_Id)

        # PROCESS - Updates value if (key, value) already present.
        for key_value in enumerate(bucket):
            
            if key_value[0] == package_Id:
                key_value[1] = value
                return True
        
        # If the (key, value) pair is new and hashes to a non-empty bucket, it will append to the list in the bucket.
        new_key_value = [package_Id, value]
        bucket.append(new_key_value)
        return True


    # RUBRIC - Section B of rubric look-up function.
        # FLOW - Searches for a value in a hash table bucket matching the given key .
    def search_item(self, key):
        '''
        Searches for value matching a given key in a bucket. Returns value if found, else None.

         Args:
            key: The key to search for in the hash table. Will accept package ID. 

        Returns:
            The value associated with the given key if found, otherwise returns None.
        '''
        
        # PROCESS - Gets the hash bucket of the corresponding key passed in.
        bucket = self.get_hash_bucket(key)

        # PROCESS - Searches for key in bucket.
        for key_value in bucket:
            
            if key_value[0] == key:
                return key_value[1]
            
        print(f"ERROR Key:Value pair for searched {key} not found.")
        return None


    # FLOW - Retrieves the specific bucket list at the hash index.
    def get_hash_bucket(self, key):
        """
        Given a key, returns the bucket at the hash index of the key.

        Parameters:
        - key: The key used to calculate the hash index.

        Returns:
        - hash_bucket: The bucket at the hash index of the key.
        """

        # PROCESS - Calculates the hash index of the key using built in python hash() function.
        hash_index = hash(key) % self.length # takes modulus of length so hash within bounds.
        
        # PROCESS - Retrieves the bucket at the hash index from hash table.
        hash_bucket = self.hash_array[hash_index]

        return hash_bucket