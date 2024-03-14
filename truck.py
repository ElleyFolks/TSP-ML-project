
import datetime as dt
from package import Package
from hash_Table import hash_Table
from hub import Hub

'''
This class represents a deliver truck that delivers packages.
The initial location of the truck is at the central HUB.
It contains attributes of the packages on the truck, the time the truck left the hub, time taken to deliver, milage traveled by truck, and current location of truck.
It contains the method for package delivery.
'''
class Delivery_Truck:
    # Constructor - Initializes attributes of the truck.
    def __init__(self, packages:list = None, time_left_hub = None):
        self.truck_package_list = packages

        # TODO refactor later to departure_time or something like that
        self.time_left_hub = time_left_hub 
        self.time = time_left_hub
        self.miles = 0

        # initial location at HUB
        self.current_location = "HUB"
        return

    '''
    Function that implements greedy algorithm.
    Removes a package from package hash table when delivered.
    Tracks truck distance and time of each delivery.
    '''
    def deliver_packages(self, package_hash_table: hash_Table, hub_hash_table: hash_Table):
        current_time = self.time_left_hub
        current_location = self.current_location

        # loops while truck still has packages
        while len(self.truck_package_list) > 0:
            min_distance = float(1000)
            min_package: Package = None

            # searching through packages for package with least distance
            for id in self.truck_package_list:
                package:Package = package_hash_table.search_item(id)
                destinationHub: Hub = hub_hash_table.search_item(package.getDestinationAddress())
                
                # gets distance from desination hub
                distance = destinationHub.getDistance(current_location)
                
                # gets distance from current hub
                if(distance == None):
                    currentHub: Hub = hub_hash_table.search_item(current_location)
                    distance = currentHub.getDistance(package.getDestinationAddress())

                distance = float(distance)

                print(f"\nPackage: {package.packageId}, Location: {current_location}, Destination: {destinationHub.address}, Distance: {distance}")

                # tests for package with least distance
                if distance < min_distance:
                    min_distance = distance
                    min_package = package

                    print("-Minimum Distance Found:",min_distance,"\n")

            # Calculate delivery time
            current_time = current_time + dt.timedelta(hours= min_distance/18)
            min_package.deliveryTime = current_time
            min_package.status = "Delivered"
            min_package.departureTime = self.time_left_hub

            # removes package that was delivered from truck
            self.truck_package_list.remove(min_package.packageId)
            
            # tracks distance and location of truck
            self.miles += min_distance
            current_location = min_package.getDestinationAddress()

            print(f"\n----Package delivered!----\n Package ID: {min_package.packageId}, Time: {min_package.deliveryTime}," 
                  f"Deadline: {min_package.deadline}, Current Location: {current_location}, Miles traveled so far: {self.miles}")