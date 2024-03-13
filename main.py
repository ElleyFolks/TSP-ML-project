from package import Package
from hub import Hub
from hash_Table import hash_Table

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
    print("Current location: ", currentHub.location)
    print("Destination: ", destinationHub.location)
    print("Distance: ",distance)


if __name__ == "__main__":
    main()