
# Class that manages hash table, uses chaining to handle collisions
class hash_Table:
    def __init__(self, length = 40):
        
        self.length = length
        self.hash_array = [None] * self.length

    # Retrieves the specific bucket list at the hash index
    def get_hash_bucket(self, key):
        hash_index = hash(key) % len(self.hash_array)
        hash_bucket = self.hash_array[hash_index]
        return hash_bucket

    # Inserts a new (key, value), or if key exists in hash bucket, will update value. Returns true if successful.
    def insert_item(self, key, value):
        
        bucket = self.get_hash_bucket(key)

        # Updates value if (key, value) already present
        for key_value in bucket:
            
            if key_value[0] == key:
                print("Inserted key value pairs: "+ key_value)
                key_value[1] = value
                return True
        
        # If (key, value) not already present, appends to end of list in bucket.
        new_key_value = [key, value]
        bucket.append(new_key_value)
        return True

    # Searches for value matching a given key in a bucket. Returns value if found, else None.
    def search_item(self, key):
        
        bucket = self.get_hash_bucket(key)

        for key_value in bucket:
            
            if key_value[0] == key:
                print("Found key value pair: "+ key_value)
                return key_value[1]
            
        return None

    def remove_item(self, key):

        bucket = self.get_hash_bucket(key)

        for key_value in bucket:
            
            if key_value[0] == key:
                print("Removed key value pair: "+ key_value)
                bucket.remove([key_value[0], key_value[1]])



