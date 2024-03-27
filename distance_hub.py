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
        '''
        Initializes a Hub object.

        Args:
            location (str): The location of the hub.
            address (str): The address of the hub.
            distances (float): The distances associated with the hub.

        Returns:
            None
        '''
        self.location = location
        self.address = address
        self.distances = distances


    # FLOW - Gets distance from hub of a specific package address. Used in greedy algorithm to determine the closest hub.
    def get_distance(self, destination_address: str):
        '''
        Gets distance from hub to a destination address. Returns distance if address is found, otherwise None.

        Parameters:
        - destination_address (str): The address of the destination from the hub.

        Returns:
        - destination_distance (float or None): The distance from the hub to the destination address, or None if the address is not found.
        '''

        #PROCESS - Iterates through the distances list to find the target address.
        for hub_address, destination_distance in self.distances:
            
            if hub_address == destination_address:
                return destination_distance
    
        return None


    # FLOW - Reads in hub information from a CSV, populates a hash table with this info. Each row becomes a hub object.
    def import_hubs(hub_hash_table:hash_table):
        '''
        Imports hub information from a CSV file and inserts hub objects into a hash table.

        Parameters:
        hub_hash_table (hash_table): The hash table to insert the hub objects into.

        Returns:
        None
        '''

        with open("WGUPS Distance Table.csv") as csv_file:
            
            # PROCESS - Reads in a CSV file into a list.
            csv_reader = csv.reader(csv_file, delimiter=",")
            hub_address = []
            distances_list = []

            # PROCESS - Iterates through each row in the CSV file to read in distance table information.
            for row in csv_reader:
                location, address, *distances = row
                hub_address.append(address)

                distances_list = list(zip(hub_address, distances))

                hub_hash_table.insert_item(address, Hub(location, address, distances_list))