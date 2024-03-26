# IDENTIFICATION - Name: Elley Folks, Student ID: 010139574 

import datetime as dt
from package import Package
from hash_Table import hash_table
from hub import Hub


class Delivery_Truck:
    '''
    This class represents a delivery truck that delivers packages.
    
    The initial location of the truck is at the central HUB.
    
    It contains attributes of the packages loaded on the truck, the time the truck left the central HUB, time taken to deliver, milage traveled by truck, and current location of truck.
    It contains the method for package delivery (GREEDY Algorithm).
    '''

    def __init__(self, packages:list = None, truck_departure_time = None):
        """
        Initializes a Truck object.
        Uses packages 'loaded' onto truck with a list passed in, and the truck's departure time from the central HUB.

        Args:
            packages (list, optional): A list of packages to be loaded onto the truck. Defaults to None.
            truck_departure_time (datetime, optional): The departure time of the truck. Defaults to None.
        """
        
        # Initializing attributes.
        packages.sort()
        self.truck_package_list = packages
        self.initial_package_list = packages.copy()
        self.truck_departure_time = truck_departure_time 
        self.miles_traveled = 0

        # Initial truck location at HUB.
        self.initial_location = "HUB"
        return


    # FLOW - Function that delivers packages to their destination.
    def deliver_packages(self, package_hash_table: hash_table, hub_hash_table: hash_table):
        '''
        Function that implements GREEDY algorithm to deliver packages to their destination.
        
        Tracks truck distance and time of each delivery. Removes a package from package list when delivered.

        Args:
            package_hash_table (hash_Table): Hash table containing packages.
            hub_hash_table (hash_Table): Hash table containing information about hub locations.

        Returns:
            None. This function modifies the package_hash_table in place, updating the status of delivered packages and tracking delivery metrics.
        '''
        
        # Initializing truck location and time for greedy algorithm.
        route_travel_time = self.truck_departure_time
        truck_location = self.initial_location

        # GREEDY ALGORITHM - Loops while truck still has packages to deliver.
        while len(self.truck_package_list) > 0:
            least_distance = float(5000)
            nearest_package: Package = None

            # PROCESS - Searches through packages for package with least distance.
            for package_id in self.truck_package_list:
                package:Package = package_hash_table.search_item(package_id)
                destinationHub: Hub = hub_hash_table.search_item(package.get_formatted_address())

                # PROCESS - Gets distance from truck's current location to package destination hub
                package_distance = destinationHub.get_distance(truck_location)
                
                # PROCESS - Protection in the case that the distance is empty.
                if(package_distance == None):
                    package_hub: Hub = hub_hash_table.search_item(truck_location)
                    package_distance = package_hub.get_distance(package.get_formatted_address())

                package_distance = float(package_distance) # type conversion for comparison

                # PROCESS - Tests for package with least distance.
                if package_distance < least_distance:
                    least_distance = package_distance
                    nearest_package = package

            # PROCESS - Calculates delivery time. Updates truck location, package status, and departure time.
            route_travel_time = route_travel_time + dt.timedelta(hours= least_distance/18)
            nearest_package.delivery_time = route_travel_time
            nearest_package.delivery_status = "DELIVERED"
            nearest_package.departure_time = self.truck_departure_time
            self.miles_traveled += least_distance
            truck_location = nearest_package.get_formatted_address()

            # PROCESS - Removes package from list that was delivered.
            self.truck_package_list.remove(nearest_package.package_id)
            
            
            