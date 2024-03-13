

'''
Class that manages a hash table, uses chaining to handle collisions.
The length / size of the hash table can be set in the params.
Contains methods to insert or update, search for, and delete items from the hash table.
'''
class hash_Table:
    
    # Constructor - Initializes the hash table to the desired length, with an empty list initialized in each of the buckets.
    def __init__(self, length:int = 40):
        
        self.length = length
        self.hash_array = [[] for _ in range(self.length)]

    # Retrieves the specific bucket list at the hash index.
    def get_hash_bucket(self, key):
        hash_index = hash(key) % self.length
        hash_bucket = self.hash_array[hash_index]
        return hash_bucket

    # Inserts a new (key, value), or if key exists in hash bucket, will update value. Returns true if successful.
    def insert_item(self, key, value):
        
        bucket = self.get_hash_bucket(key)

        # updates value if (key, value) already present
        for key_value in enumerate(bucket):
            
            if key_value[0] == key:
                print("--------------------------------")
                print("Inserted key value pairs:")
                print("Key:",key_value[0],"\n")
                print("Package information:", key_value[1], "\n")
                print("--------------------------------")
                key_value[1] = value
                return True
        
        # CHAINING - if (key, value) not already present, appends to end of list in bucket.
        new_key_value = [key, value]
        bucket.append(new_key_value)
        return True

    # Searches for value matching a given key in a bucket. Returns value if found, else None.
    def search_item(self, key):
        
        bucket = self.get_hash_bucket(key)

        for key_value in bucket:
            
            if key_value[0] == key:
                print("--------------------------------")
                print("Searched and found key value pair:")
                print("Item searched:",key_value[0],"\n")
                print("Package information:", key_value[1], "\n")
                print("--------------------------------")

                return key_value[1]
        print("ERROR Key:Value pair not found.")
        return None

    # Removes an item from hash table if the searched key matches an existing key in a bucket.
    def remove_item(self, key_to_delete):

        bucket = self.get_hash_bucket(key_to_delete)

        for key_value in bucket:
            
            if key_value[0] == key_to_delete:
                print("--------------------------------")
                print("Removed key value pair:")
                print("Item searched:",key_value[0],"\n")
                print("Package information:", key_value[1], "\n")
                print("--------------------------------")

                bucket.remove([key_value[0], key_value[1]])

    # Prints out each bucket of hash table.
    def print_hash_table(self):
        for index, bucket in enumerate(self.hash_array):
            if bucket:
                print(f"Bucket {index}:")
                for key, value in bucket:
                    print(f"{key} : {value}")

            else:
                print(f"Bucket {index}: Empty")

