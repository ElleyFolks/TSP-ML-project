# IDENTIFICATION - Name: Elley Folks, Student ID: 010139574 

import csv
from hash_Table import hash_table

class Hub:
    '''
    The class the represents a hub location. 
    The hub contains the name of a location, address, and distances from this location to every other location.
    This class implements methods to initialize, import hubs from a CSV file,
    and a method to get the distance from one point to another.
    '''

    # Constructor - Initializes location, address and distances from every other location to this one.
    def __init__(self, location: str, address: str, distances: float):
        """
        Initializes a Hub object.

        Args:
            location (str): The location of the hub.
            address (str): The address of the hub.
            distances (float): The distances associated with the hub.

        Returns:
            None
        """
        self.location = location
        self.address = address
        self.distances = distances

    # A string representation of a hub object, formatted to print location, address and distances.
    def __str__(self):
            return f"Location: {self.location}, Address: {self.address}, Distance List: {self.distances}"
    
    # FLOW - Gets distance from hub of a target address. Used in greedy algorithm to determine the closest hub.
    def get_distance(self, target_hub_address: str):
            '''
            Gets distance from hub of a target address. Returns distance if address is found, otherwise None.

            Parameters:
            - target_hub_address (str): The address of the target hub.

            Returns:
            - distance (float or None): The distance from the hub to the target address, or None if the address is not found.
            '''
            # TODO refactor this to look different

            #PROCESS - Iterates through the distances list to find the target address.
            for hub_address, distance in self.distances:
                if hub_address == target_hub_address:
                    return distance
                
            return None

    # FLOW - Reads in hub information from a CSV, populates a hash table with this info. Each row becomes a hub object.
    def import_hubs(hubHashTable:hash_table):
        
        # TODO refactor this to look different
        with open("WGUPS Distance Table.csv") as csv_file:
            
            # PROCESS - Reads in a CSV file into a list.
            csv_reader = csv.reader(csv_file, delimiter=",")
            hub_address = []

            # PROCESS - Iterates through each row in the CSV file and creates a hub object.
            for row in csv_reader:
                location, address, *distances = row
                hub_address.append(address)
                distances = list(zip(hub_address, distances))
                
                # PROCESS - Inserts hub object into the hash table.
                hub = Hub(location, address, distances)
                hubHashTable.insert_item(hub.address, hub)