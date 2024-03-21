# IDENTIFICATION - Name: Elley Folks, Student ID: 010139574 

import datetime as dt
from package import Package
from hash_Table import hash_Table
from hub import Hub


class Delivery_Truck:
    '''
    This class represents a deliver truck that delivers packages.
    The initial location of the truck is at the central HUB.
    It contains attributes of the packages on the truck, the time the truck left the hub, time taken to deliver, milage traveled by truck, and current location of truck.
    It contains the method for package delivery.
    '''
    # Constructor - Initializes attributes of the truck.
    def __init__(self, packages:list = None, truck_departure_time = None):
        self.truck_package_list = packages
        self.truck_departure_time = truck_departure_time 
        self.time = truck_departure_time
        self.miles = 0

        # initial location at HUB
        self.current_location = "HUB"
        return

    
    def deliver_packages(self, package_hash_table: hash_Table, hub_hash_table: hash_Table):
        '''
        Function that implements greedy algorithm.
        Removes a package from package list when delivered.
        Tracks truck distance and time of each delivery.

        Args:
            package_hash_table (hash_Table): Hash table containing packages.
            hub_hash_table (hash_Table): Hash table containing information about hub locations.

        Returns:
            None. This function modifies the package_hash_table in place, updating the status of delivered packages and tracking delivery metrics.
        '''
        present_time = self.truck_departure_time
        present_location = self.current_location

        # GREEDY ALGORITHM - loops while truck still has packages
        while len(self.truck_package_list) > 0:
            minimum_distance : float = float(1000)
            package_to_deliver: Package = None

            # searching through packages for package with least distance
            for id in self.truck_package_list:
                package:Package = package_hash_table.search_item(id)
                destinationHub: Hub = hub_hash_table.search_item(package.getDestinationAddress())
                
                # gets distance from destination hub
                package_distance = destinationHub.getDistance(present_location)
                
                # protection in the case that distance is empty
                if(package_distance == None):
                    package_hub: Hub = hub_hash_table.search_item(present_location)
                    package_distance = package_hub.getDistance(package.getDestinationAddress())

                package_distance = float(package_distance)

                # tests for package with least distance
                if package_distance < minimum_distance:
                    minimum_distance = package_distance
                    package_to_deliver = package

            # Calculate delivery time
            present_time = present_time + dt.timedelta(hours= minimum_distance/18)
            package_to_deliver.delivery_time = present_time
            package_to_deliver.delivery_status = "DELIVERED"
            package_to_deliver.departure_time = self.truck_departure_time

            # removes package that was delivered from truck
            self.truck_package_list.remove(package_to_deliver.packageId)
            
            # tracks distance and location of truck
            self.miles += minimum_distance
            present_location = package_to_deliver.getDestinationAddress()