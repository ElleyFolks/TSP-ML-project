# IDENTIFICATION - Name: Elley Folks, Student ID: 010139574 

import csv
from hash_Table import hash_table

class Package:
    '''
    Class that represents a package.
    The package object has the information imported from the WGUPS Package CSV file, which has the following attributes:
    package ID, address, city, state, zip, date to be delivered by, and package weight.

    The delivery time and departure time are set in the delivery function when a package is en route and delivered, and are not found in the package file.

    This class implements methods to read in package information from a CSV, create new package objects, and get the package destination address.
    '''

    def __init__(self, package_id, address, city, state, zip_code, deadline, weight):
        """
        Initializes a Package object with the package information.

        Args:
            package_id (int): The ID of the package.
            address (str): The address of the package.
            city (str): The city of the package.
            state (str): The state of the package.
            zip_code (str): The ZIP code of the package.
            deadline (str): The delivery deadline for the package.
            weight (float): The weight of the package.

        Attributes:
            package_id (int): The ID of the package.
            address (str): The address of the package.
            city (str): The city of the package.
            state (str): The state of the package.
            zip_code (str): The ZIP code of the package.
            deadline (str): The delivery deadline of the package.
            weight (float): The weight of the package.
            present_Location (str): The current location of the package (initialized to "HUB").
            delivery_status (str): The delivery status of the package (initialized to "HUB").
            departure_time (str): The departure time of the package (initialized to None).
            delivery_time (str): The delivery time of the package (initialized to None).
        """
        # Loaded from CSV.
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.weight = weight
        self.present_Location = "HUB"
        
        # These are set separately outside of this class.
        self.delivery_status = "HUB"
        self.departure_time = None
        self.delivery_time = None

    # FLOW - Returns a string representation of a package object when called.
    def __str__(self):
        '''
        A string representation of a package object, formatted to print all package information.

        Returns:
            str: A formatted string containing all package information.
        '''
        package_status:str = f"Package ID: {self.package_id}, Delivery Status: {self.delivery_status}, Departure time from HUB: {self.departure_time} Deadline: {self.deadline},  Anticipated Time Delivered: {self.delivery_time}, Weight: {self.weight} lbs\n"
        package_local:str = f"Current Location: {self.present_Location}, Destination Address: {self.address}, {self.city}, {self.state}, {self.zip_code}\n"
        return package_status + package_local


    # FLOW - Creates a package object from a each row of the CSV.
    def create_package(row):
        """
        Create a Package object from a row of data.

        Args:
            row (list): A list containing the package data.

        Returns:
            Package: The created Package object.
        """

        # PROCESS - Unpacks the row into the package attributes.
        package_id, package_address, package_city, package_state, package_zip, package_deadline, package_weight = row[:7]
        
        return Package(int(package_id), package_address, package_city, package_state, package_zip, package_deadline, package_weight)
    

    # FLOW - Imports info from entire CSV, and creates a new package per row.
    def import_package(package_hash_table: hash_table):
        """
        Imports package data from a CSV file, creates package object with all information, then inserts package object into hash table.

        Args:
            package_hash_table (hash_table): The hash table to insert the packages into.

        Returns:
            None
        """
        # PROCESS - Reads in the CSV file.
        with open("WGUPS Package File.csv") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            
            # PROCESS - Iterates through each row in CSV file to create a package object.
            for row in csv_reader:
                package = Package.create_package(row)
                package_hash_table.insert_item(package.package_id, package)
    

    # FLOW - Gets address of package destination. Used in delivery algorithm to determine destination of a package.
    def get_formatted_address(self):
            """
            Gets destination address of package.

            Returns:
                str: The destination address of a package, includes zip code.
            """
            return self.address + f" ({self.zip_code})"
