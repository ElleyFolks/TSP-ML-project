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
    
        self.delivery_truck_1 : Delivery_Truck  = truck_1
        self.delivery_truck_2 : Delivery_Truck = truck_2
        self.delivery_truck_3 : Delivery_Truck = truck_3
        
        self.total_miles : int = total_milage

        self.packageHashTable : hash_table = package_hash_table

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

            if user_choice =='3':
                print(f"*--__-- Total milage traveled by all delivery trucks {self.total_miles} miles. --__--*")
            
            elif user_choice == '4':
                using_menu = False
                print("*--__-- Thankyou for shipping with WGUPS! Exiting program. --__--*")
                exit()

    def generate_report_all_packages(self):
        # PROCESS - Gets time from user.
        user_time_str:str = input("        Please enter the time (24 hour HH:mm:ss) you want to see the status of all packages.\n")
        (entered_hrs, entered_min, entered_sec) = user_time_str.split(':')
        
        user_time = dt.timedelta(hours = int(entered_hrs), minutes= int(entered_min), seconds= int(entered_sec))

        # PROCESS - Gets info for packages on truck 1.
        print(f"\n--__-- Truck 1 package list: {self.delivery_truck_1.initial_package_list} --__--\n")
        for id in self.delivery_truck_1.initial_package_list:
            searched_package:Package = self.packageHashTable.search_item(id)

            # Package at hub, not in transit.
            if user_time <= searched_package.departure_time:
                print(f"-----| Package {searched_package.packageId} status - AT HUB |-----")
                
                if searched_package.packageId == 9:
                    self.print_package_9_info(user_time, searched_package)

                else:
                    self.print_package_status(searched_package)

            # Package in transit.
            elif searched_package.departure_time < user_time < searched_package.delivery_time:
                print("-->--> Package status - EN ROUTE -->-->")
                
                if searched_package.packageId == 9:
                    self.print_package_9_info(user_time, searched_package)

                else:
                    self.print_package_status(searched_package)
            
            # Package delivered.
            else:
                print("-->--x Package status - DELIVERED -->--x")
                
                if searched_package.packageId == 9:
                    self.print_package_9_info(user_time, searched_package)

                else:
                    self.print_package_status(searched_package)
            print("\n")
    

    def generate_report_for_package(self):
        # PROCESS - Gets time from user.
        user_time_str:str = input("        Please enter the time (24 hour HH:mm:ss) you want to see the status of a package.\n")
        (entered_hrs, entered_min, entered_sec) = user_time_str.split(':')
        
        user_time = dt.timedelta(hours = int(entered_hrs), minutes= int(entered_min), seconds= int(entered_sec))

        # PROCESS - Getting package ID from user.
        user_package_id: int = int(input("        Enter the package ID.\n"))

        # Gets info for one package
        if 0 < user_package_id < 41:
            searched_package:Package = self.packageHashTable.search_item(user_package_id)

            # Package at hub, not in transit.
            if user_time <= searched_package.departure_time:
                print("-----| Package status - AT HUB |-----")
                
                if searched_package.packageId == 9:
                    self.print_package_9_info(user_time, searched_package)

                else:
                    self.print_package_status(searched_package)

            # Package in transit.
            elif searched_package.departure_time < user_time < searched_package.delivery_time:
                print("-->--> Package status - EN ROUTE -->-->")
                
                if searched_package.packageId == 9:
                    self.print_package_9_info(user_time, searched_package)

                else:
                    self.print_package_status(searched_package)

            # Package delivered.
            else:
                print("-->--x Package status - DELIVERED -->--x")
                
                if searched_package.packageId == 9:
                    self.print_package_9_info(user_time, searched_package)

                else:
                    self.print_package_status(searched_package)
        else:
            raise ValueError("Not a valid package ID. Must be from 1 - 40.")

    # FLOW - Prints package status.
    def print_package_status(self, searched_package:Package):
        print(f"        Package ID: {searched_package.packageId}. \n       Delivery time: {searched_package.delivery_time}.",
            f"\n       Must be delivered to the address: {searched_package.address} {searched_package.city} {searched_package.state} {searched_package.zipCode}", 
            f"\n       by {searched_package.deadline}")
        
    # FLOW - Prints package 9 to correct package address after 10:20 AM.
    def print_package_9_info(self, user_time:dt, package:Package):
            
                corrected_time = dt.timedelta(hours=10, minutes=20)
                                        
                if user_time < corrected_time:
                    print(f"        Package ID: {package.packageId}. \n       Delivery time: {package.delivery_time}.",
                        f"\n       Must be delivered to the address: {package.address} {package.city} {package.state} {package.zipCode}", 
                        f"\n       by {package.deadline}"
                        )
                    
                if user_time>= corrected_time:
                    print(f"        Package ID: {package.packageId}. \n       Delivery time: {package.delivery_time}.",
                        f"\n       Must be delivered to the address: 410 S. State St., Salt Lake City, UT 84111", 
                        f"\n       by {package.deadline}"
                        )