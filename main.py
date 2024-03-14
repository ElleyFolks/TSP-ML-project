import datetime as dt
from package import Package
from hub import Hub
from hash_Table import hash_Table
from truck import Delivery_Truck

def main( args = ""):
    
    # creating hash tables, storing data from CSVs into buckets
    packageHashTable = hash_Table(length=40)
    Package.importPackages(packageHashTable)
    #packageHashTable.print_hash_table()

    hubHashTable = hash_Table(length=30)
    Hub.importHubs(hubHashTable)
    #hubHashTable.print_hash_table()

    package = packageHashTable.search_item(13)
    currentHub = hubHashTable.search_item(package.currentLocation)
    destinationHub = hubHashTable.search_item(package.getDestinationAddress())
    distance = destinationHub.getDistance(currentHub.address)
    #print("Current location: ", currentHub.location)
    #print("Destination: ", destinationHub.location)
    #print("Distance: ",distance)


    # loading packages onto trucks via package ID
    load_1: list = [1, 13, 5, 14, 15, 16, 19, 20, 29, 30, 31, 37, 40]
    delivery_truck_1 : Delivery_Truck = Delivery_Truck(load_1, time_left_hub = dt.timedelta(hours= 8))

    # delivering packages
    delivery_truck_1.deliver_packages(packageHashTable, hubHashTable)


if __name__ == "__main__":
    main()