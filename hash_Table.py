
# Class that manages hash table, uses chaining to handle collisions
class hash_Table:
    def __init__(self, length = 40):
        
        self.length = length
        self.hash_array = [None] * self.length

    # Inserts a new (key, value), or if key exists in hash bucket, will update value. Returns true if successful.
    def insert_item(self, key, value):
        
        hash_index = hash(key) % len(self.hash_array)
        
        # Retrieves the specific bucket list at the hash index
        hash_bucket = self.hash_array[hash_index]

        # Updates value if (key, value) already present
        for key_value in hash_bucket:
            print("New key value pair: "+ key_value)
            
            if key_value[0] == key:
                kv[1] = value
                return True
        
        # If (key, value) not already present, appends to end of list in bucket.
        new_key_value = [key, value]
        hash_bucket.append(new_key_value)
        return True


