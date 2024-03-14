import csv
from hash_Table import hash_Table

'''
Class that represents a package.
The package object has the information imported from the WGUPS Package CSV file, which has the following attributes:
package ID, address, city, state, zip, date to be delivered by, and package weight.

The delivery time and departure time are set elsewhere, and are not in the package file.

This class implements methods to read in package information from a CSV, create new package objects, and get the package destination address.
'''
class Package:
    # Constructor - Initializes attributes of package object.
    def __init__(self, packageId, address, city, state, zipCode, deadline, weight):
        # loaded from CSV
        self.packageId = packageId
        self.address = address
        self.city = city
        self.state = state
        self.zipCode = zipCode
        self.deadline = deadline
        self.weight = weight
        self.currentLocation = "HUB"
        
        # these are set separately outside of this class
        self.status = "HUB"
        self.departureTime = None
        self.deliveryTime = None

    # A string representation of a package object, formatted to print all package information.
    def __str__(self):
        return f"Package ID: {self.packageId}, Address: {self.address}, {self.city}, {self.state}, {self.zipCode}, Deadline: {self.deadline}, Weight: {self.weight} lbs, Current Location: {self.currentLocation}, Departure Time: {self.departureTime}, Deliver Time: {self.deliveryTime}"

    # Creates a package object from a row passed in of the CSV.
    def createNewPackage(row):
        pId, pAddress, pCity, pState, pZip, pDeadline, pWeight = row[:7]
        return Package(int(pId), pAddress, pCity, pState, pZip, pDeadline, pWeight)
    
    # Creates a new package per row, for every row in CSV.
    def importPackages(package_hash_table: hash_Table):
        with open("WGUPS Package File.csv") as csvFile:
            csvReader = csv.reader(csvFile, delimiter=",")
            for row in csvReader:
                newPackage = Package.createNewPackage(row)
                package_hash_table.insert_item(newPackage.packageId, newPackage)
    
    # Gets address of package destination.
    def getDestinationAddress(self):
        return self.address + f" ({self.zipCode})"