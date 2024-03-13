
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
    def __init__(self, packages = None, time_left_hub = None):
        self.packages = packages
        self.time_left_hub = time_left_hub
        self.time = time_left_hub
        self.miles = 0

        # initial location at HUB
        self.current_location = "4001 South 700 East"
        return

    '''
    Function that implements greedy algorithm.
    Removes a package from package hash table when delivered.
    Tracks truck distance and time of each delivery.
    '''
    def deliver_packages(self,truck, packages: hash_Table):
        current_time = self.time_left_hub
        self.current_location = self.current_location

        while len(self.packages) > 0: # while loop for truck has packages
            min_distance = 1000
            min_package = None
            for id in truck.packages:# searches for package
                package = packages.search(id)
                distance = Hub.getDistance(package.address)
                if distance < min_distance:
                    min_distance = distance
                    min_package = package

            # Calculate delivery time
            current_time = current_time + dt.timedelta(hours= min_distance/18)
            min_package.delivery_time = current_time
            min_package.status = "Delivered"
            min_package.left_hub = truck.time_left_hub
            truck.packages.remove(min_package.id)
            truck.miles += min_distance
            self.current_location = min_package.address