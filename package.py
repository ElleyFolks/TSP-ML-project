import csv
class Package:
    def __init__(self, packageId, address, city, state, zipCode, deadline, weight):
        self.packageId = packageId
        self.address = address
        self.city = city
        self.state = state
        self.zipCode = zipCode
        self.deadline = deadline
        self.weight = weight
        self.currentLocation = "HUB"
        self.deliveryTime = None
        self.departureTime = None

    def __str__(self):
        return f"Package ID: {self.packageId}, Address: {self.address}, {self.city}, {self.state}, {self.zipCode}, Deadline: {self.deadline}, Weight: {self.weight} lbs, Current Location: {self.currentLocation}, Departure Time: {self.departureTime}, Deliver Time: {self.deliveryTime}"

    # Instantiates a new package object based on a row read in from CSV
    def createNewPackage(row):
        pId, pAddress, pCity, pState, pZip, pDeadline, pWeight = row[:7]
        return Package(int(pId), pAddress, pCity, pState, pZip, pDeadline, pWeight)
    
    # Reads in CSV file and 
    def importPackagesFromCSV():
        with open("WGUPS Package File.csv") as csvFile:
            csvReader = csv.reader(csvFile, delimiter=",")
            for row in csvReader:
                newPackage = Package.createNewPackage(row)
                print(newPackage)