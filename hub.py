# IDENTIFICATION - Name: Elley Folks, Student ID: 010139574 

import csv
from hash_Table import hash_Table

class Hub:
    '''
    The class the represents a hub location. 
    The hub contains the name of a location, address, and distances from this location to every other location.
    This class implements methods to initialize, import hubs from a CSV file,
    and a method to get the distance from one point to another.
    '''

    # Constructor - Initializes location, address and distances from every other location to this one.
    def __init__(self, location: str, address: str, distances: float):
        self.location = location
        self.address = address
        self.distances = distances

    # A string representation of a hub object, formatted to print location, address and distances.
    def __str__(self):
        return f"Location: {self.location}, Address: {self.address}, Distance List: {self.distances}"
    
    # Gets distance from hub of a target address. Returns distance if address is found, otherwise None.
    def getDistance(self, targetHubAddress: str):
        for hubAddress, distance in self.distances:
            if(hubAddress == targetHubAddress):
                return distance
            
        return None

    # Reads in hub information from a CSV, populates a hash table with this info. Each row becomes a hub object.
    def importHubs(hubHashTable:hash_Table):
        with open("WGUPS Distance Table.csv") as csvFile:
            csvReader = csv.reader(csvFile, delimiter=",")
            hubAddress = []
            for row in csvReader:
                location, address, *distances = row
                hubAddress.append(address)
                distances = list(zip(hubAddress, distances))
                hub = Hub(location, address, distances)
                hubHashTable.insert_item(hub.address, hub)