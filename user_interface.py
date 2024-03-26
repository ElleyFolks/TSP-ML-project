# IDENTIFICATION - Name: Elley Folks, Student ID: 010139574

# RUBRIC - Section D, Interface.

from truck import Delivery_Truck
from package import Package
from hash_Table import hash_table
import datetime as dt

class delivery_menu():
    
    # Initializing attributes.
    delivery_truck_1 : Delivery_Truck  = None
    delivery_truck_2 : Delivery_Truck = None
    delivery_truck_3 : Delivery_Truck = None
    total_miles : int = 0
    packageHashTable : hash_table = None

    def __init__(self, truck_1: Delivery_Truck, truck_2, truck_3, total_milage, package_hash_table):
            """
            Initializes an instance of the UserInterface class.

            Args:
                truck_1 (Delivery_Truck): The first delivery truck.
                truck_2 (Delivery_Truck): The second delivery truck.
                truck_3 (Delivery_Truck): The third delivery truck.
                total_milage (int): The total mileage of all trucks.
                package_hash_table (hash_table): The hash table containing package information.
            """
        
            self.delivery_truck_1 : Delivery_Truck  = truck_1
            self.delivery_truck_2 : Delivery_Truck = truck_2
            self.delivery_truck_3 : Delivery_Truck = truck_3
            self.total_miles : int = total_milage
            self.packageHashTable : hash_table = package_hash_table


    # FLOW - User menu for selecting options.
    def user_menu(self):

        using_menu: bool = True

        # FLOW - User types in number to select option from menu.
        while(using_menu == True):
            print("        Please select an option below.", "\n")
            print("        1 -- View ALL packages / delivery status in a given time range.")
            print("        2 -- View ONE package / delivery status in a given time range.")
            print("        3 -- View total milage of all trucks.")
            print("        4 -- Exit program.")
            user_choice = input("        Enter the number (1, 2, or 3) of the option you want to select.\n")

            # PROCESS - Option 1, generating status report for all packages at a given time.
            if user_choice == '1':
                try:
                    self.generate_report_all_packages()
                except ValueError:
                    print("--X-- Not an option. Returning to main menu. --X--")  

            # PROCESS - Option 2, generating status report for one package at a given time.
            if user_choice == '2':
                try:
                    self.generate_report_for_package()
                except ValueError:
                    print("--X-- Not a valid package ID. Must be from 1 - 40. Returning to main menu. --X--")

            # PROCESS - Option 3, displaying total milage of all trucks.
            if user_choice =='3':
                print(f"*--__-- Total milage traveled by all delivery trucks {self.total_miles} miles. --__--*")
            
            # PROCESS - Option 4, exiting program.
            elif user_choice == '4':
                using_menu = False
                print("*--__-- Thankyou for shipping with WGUPS! Exiting program. --__--*")
                exit()
            
            # PROCESS - Invalid option entered.
            else:
                print("--X-- Not an option. Please enter a valid option. --X--\n")


    # FLOW - Gets time from user.
    def get_user_time(self):
        # PROCESS - Gets time string from user.
        user_time_str:str = input("        Please enter the time (24 hour HH:mm:ss) you want to see the status package(s).\n")
        
        # PROCESS - Splits time string into hours, minutes, and seconds, separated by the ':'.
        (entered_hrs, entered_min, entered_sec) = user_time_str.split(':')
        
        user_time_dt = dt.timedelta(hours = int(entered_hrs), minutes= int(entered_min), seconds= int(entered_sec))
        return user_time_dt


    # FLOW - Generates report for all packages at a given time.
    def generate_report_all_packages(self):
        '''
        Creates a report for all packages, showing individual status at a time entered by user. 
        
        The packages are separated by truck. This report displays delivery status, delivery time, address, city, state, zip code and deadline.
        '''

        desired_time = self.get_user_time()
        truck_list = [self.delivery_truck_1, self.delivery_truck_2, self.delivery_truck_3]
        
        # PROCESS - Gets info for packages on truck each truck.
        for truck_number, truck_list in enumerate(truck_list, start=1):
            print(f"\n--__-- Truck {truck_number} package list: {truck_list.initial_package_list} --__--\n")
            
            # PROCESS - Searches package hash table for information on each package.
            for id in truck_list.initial_package_list:
                searched_package:Package = self.packageHashTable.search_item(id)

                # Package at hub, not in transit.
                if desired_time <= searched_package.departure_time:
                    print(f"-----| Package {searched_package.package_id} status - AT HUB |-----")
                    self.print_package_status(searched_package, desired_time)

                # Package in transit.
                elif searched_package.departure_time < desired_time < searched_package.delivery_time:
                    print("-->--> Package status - EN ROUTE -->-->")
                    self.print_package_status(searched_package, desired_time)
                
                # Package delivered.
                else:
                    print("-->--x Package status - DELIVERED -->--x")
                    self.print_package_status(searched_package, desired_time)
            
            print("\n")


    # FLOW - Generates report for one package at a given time.
    def generate_report_for_package(self):
        '''
        Creates a report for one searched package, showing package status at a time entered by user. 
        
        If the searched package is found, this report displays delivery status, delivery time, address, city, state, zip code and deadline.
        '''
        desired_time = self.get_user_time()

        # PROCESS - Getting package ID from user.
        user_package_id: int = int(input("        Enter the package ID.\n"))

        # Gets info for one package
        if 0 < user_package_id < 41:
            searched_package:Package = self.packageHashTable.search_item(user_package_id)

            # Package at hub, not in transit.
            if desired_time <= searched_package.departure_time:
                print("-----| Package status - AT HUB |-----")
                self.print_package_status(searched_package, desired_time)

            # Package in transit.
            elif searched_package.departure_time < desired_time < searched_package.delivery_time:
                print("-->--> Package status - EN ROUTE -->-->")
                self.print_package_status(searched_package, desired_time)

            # Package delivered.
            else:
                print("-->--x Package status - DELIVERED -->--x")
                self.print_package_status(searched_package, desired_time)
        else:
            raise ValueError("Not a valid package ID. Must be from 1 - 40.")


    # FLOW - Prints package status.
    def print_package_status(self, package:Package, user_time:dt):
        """
        Prints the status of a package based on the time entered by user.

        Args:
            package (Package): The package object with all information specific to that package.
            user_time (datetime): The current time provided by the user.

        Returns:
            None
        """
        
        # PROCESS - Correcting address for package 9.
        if package.package_id == 9:
            corrected_time = dt.timedelta(hours=10, minutes=20)
                                            
            if user_time < corrected_time:
                print(f"        Package ID: {package.package_id}. \n       Delivery time: {package.delivery_time}.",
                    f"\n       Must be delivered to the address: {package.address} {package.city} {package.state} {package.zip_code}", 
                    f"\n       by {package.deadline}"
                    )
                
            if user_time>= corrected_time:
                print(f"        Package ID: {package.package_id}. \n       Delivery time: {package.delivery_time}.",
                    f"\n       Must be delivered to the address: 410 S. State St., Salt Lake City, UT 84111", 
                    f"\n       by {package.deadline}"
                    )

        # PROCESS - Reporting package status normally for all other packages.
        else:
            print(f"        Package ID: {package.package_id}. \n       Delivery time: {package.delivery_time}.",
                f"\n       Must be delivered to the address: {package.address} {package.city} {package.state} {package.zip_code}", 
                f"\n       by {package.deadline}")
        
   