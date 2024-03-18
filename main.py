import datetime as dt
from package import Package
from hub import Hub
from hash_Table import hash_Table
from truck import Delivery_Truck

# creating hash tables, storing data from CSVs into buckets
packageHashTable = hash_Table(length=40)
Package.importPackages(packageHashTable)

hubHashTable = hash_Table(length=30)
Hub.importHubs(hubHashTable)

def main():

    # loading packages onto trucks via package ID
    load_1: list = [1, 13, 5, 14, 15, 16, 19, 20, 29, 30, 31, 37, 40]
    delivery_truck_1: Delivery_Truck = Delivery_Truck(load_1, time_left_hub = dt.timedelta(hours= 8)) # leaves right at 8:00AM

    load_2: list = [2, 3, 4, 7, 8, 18, 25, 32, 34, 6, 28, 36, 38]
    delivery_truck_2: Delivery_Truck = Delivery_Truck(load_2,time_left_hub= dt.timedelta(hours=9, minutes= 30)) # leaves when packages delayed in flight arrive

    load_3: list = [9, 10, 11, 12, 17, 21, 35, 22, 23, 24, 26, 27, 33, 39]
    delivery_truck_3 = Delivery_Truck(load_3, time_left_hub= dt.timedelta(hours=10, minutes=30)) # leaves when truck driver is available 

    # delivering packages
    delivery_truck_1.deliver_packages(packageHashTable, hubHashTable)
    delivery_truck_2.deliver_packages(packageHashTable, hubHashTable)
    delivery_truck_3.deliver_packages(packageHashTable, hubHashTable)

    # combined distance traveled of each truck (must be under 140 miles)
    total_distance = delivery_truck_1.miles + delivery_truck_2.miles + delivery_truck_3.miles
    print(f"*--__-- Trucks TOTAL milage is {total_distance} miles. --__--*\n")


def print_package_9_info(user_time:dt, package:Package):
    
    corrected_time = dt.timedelta(hours=10, minutes=20)
                            
    if user_time < corrected_time:
        print(f"        Package ID: {package.packageId}. \n       Delivery time: {package.deliveryTime}.",
            f"\n       Must be delivered to the address: {package.address} {package.city} {package.state} {package.zipCode}", 
            f"\n       by {package.deadline}"
            )
        
    if user_time>= corrected_time:
        print(f"        Package ID: {package.packageId}. \n       Delivery time: {package.deliveryTime}.",
            f"\n       Must be delivered to the address: 410 S. State St., Salt Lake City, UT 84111", 
            f"\n       by {package.deadline}"
            )

def wgups_UI():

    using_menu: bool = True

    while(using_menu == True):
        print("        Please select an option below.", "\n")
        print("        1 -- View ALL packages / delivery status in a given time range.")
        print("        2 -- View ONE package / delivery status in a given time range.")
        print("        3 -- Exit program.")
        user_choice = input("        Enter the number (1, 2, or 3) of the option you want to select.\n")

        # Option 1 - generating status report for all packages at a given time
        if user_choice == '1':
            try:
                user_time_str:str = input("        Please enter the time (24 hour HH:mm:ss) you want to see the status of all packages.\n")
                (entered_hrs, entered_min, entered_sec) = user_time_str.split(':')
                
                user_time = dt.timedelta(hours = int(entered_hrs), minutes= int(entered_min), seconds= int(entered_sec))

                # gets info for packages 0 - 39 (40 total)
                for i in range(1,41):
                    searched_package:Package = packageHashTable.search_item(i)

                    # package at hub, not in transit
                    if user_time <= searched_package.departureTime:
                        
                        if searched_package.packageId == 9:
                            print("-----| Package status - AT HUB |-----")
                            print_package_9_info(user_time, searched_package)

                        else:
                            print("-----| Package status - AT HUB |-----")
                            print(f"        Package ID: {searched_package.packageId}. \n       Delivery time: {searched_package.deliveryTime}.",
                                f"\n       Must be delivered to the address: {searched_package.address} {searched_package.city} {searched_package.state} {searched_package.zipCode}", 
                                f"\n       by {searched_package.deadline}"
                                )

                    # package in transit
                    elif searched_package.departureTime < user_time < searched_package.deliveryTime:
                        
                        if searched_package.packageId == 9:
                            print("-->--> Package status - EN ROUTE -->-->")
                            print_package_9_info(user_time, searched_package)

                        else:
                            print("-->--> Package status - EN ROUTE -->-->")
                            print(f"        Package ID: {searched_package.packageId}. \n       Delivery time: {searched_package.deliveryTime}.",
                                f"\n       Must be delivered to the address: {searched_package.address} {searched_package.city} {searched_package.state} {searched_package.zipCode}", 
                                f"\n       by {searched_package.deadline}"
                                )
                    
                    # package delivered
                    else:
                        if searched_package.packageId == 9:
                            print("-->--x Package status - DELIVERED -->--x")
                            print_package_9_info(user_time, searched_package)

                        else:
                            print("-->--x Package status - DELIVERED -->--x")
                            print(f"        Package ID: {searched_package.packageId}. \n       Delivery time: {searched_package.deliveryTime}.",
                                f"\n       Must be delivered to the address: {searched_package.address} {searched_package.city} {searched_package.state} {searched_package.zipCode}", 
                                f"\n       by {searched_package.deadline}"
                                )

            except ValueError:
                print("--X-- Not an option. Returning to main menu. --X--")

        if user_choice == '2':
            try:
                # getting time
                user_time_str:str = input("        Please enter the time (24 hour HH:mm:ss) you want to see the status of a package.\n")
                (entered_hrs, entered_min, entered_sec) = user_time_str.split(':')
                
                user_time = dt.timedelta(hours = int(entered_hrs), minutes= int(entered_min), seconds= int(entered_sec))

                # getting package ID
                user_package_id: int = int(input("        Enter the package ID.\n"))

                # gets info for one package
                if 0 < user_package_id < 41:
                    searched_package:Package = packageHashTable.search_item(user_package_id)

                    # package at hub, not in transit
                    if user_time <= searched_package.departureTime:
                        
                        if searched_package.packageId == 9:
                            print("-----| Package status - AT HUB |-----")
                            print_package_9_info(user_time, searched_package)

                        else:
                            print("-----| Package status - AT HUB |-----")
                            print(f"        Package ID: {searched_package.packageId}. \n       Delivery time: {searched_package.deliveryTime}.",
                                f"\n       Must be delivered to the address: {searched_package.address} {searched_package.city} {searched_package.state} {searched_package.zipCode}", 
                                f"\n       by {searched_package.deadline}"
                                )

                    # package in transit
                    elif searched_package.departureTime < user_time < searched_package.deliveryTime:
                        
                        if searched_package.packageId == 9:
                            print("-->--> Package status - EN ROUTE -->-->")
                            print_package_9_info(user_time, searched_package)

                        else:
                            print("-->--> Package status - EN ROUTE -->-->")
                            print(f"        Package ID: {searched_package.packageId}. \n       Delivery time: {searched_package.deliveryTime}.",
                                f"\n       Must be delivered to the address: {searched_package.address} {searched_package.city} {searched_package.state} {searched_package.zipCode}", 
                                f"\n       by {searched_package.deadline}"
                                )

                    # package delivered
                    else:
                        
                        if searched_package.packageId == 9:
                            print("-->--x Package status - DELIVERED -->--x")
                            print(f"        Package ID: {searched_package.packageId}. \n       Delivery time: {searched_package.deliveryTime}.",
                                    f"\n       Must be delivered to the address: 410 S. State St., Salt Lake City, UT 84111", 
                                    f"\n       by {searched_package.deadline}"
                                    )

                        else:
                            print("-->--x Package status - DELIVERED -->--x")
                            print(f"        Package ID: {searched_package.packageId}. \n       Delivery time: {searched_package.deliveryTime}.",
                                f"\n       Must be delivered to the address: {searched_package.address} {searched_package.city} {searched_package.state} {searched_package.zipCode}", 
                                f"\n       by {searched_package.deadline}"
                                )

            except ValueError:
                print("--X-- Not a valid package ID. Must be from 1 - 40. Returning to main menu. --X--")

        elif user_choice == '3':
            using_menu = False
            print("*--__-- Thankyou for shipping with WGUPS! Exiting program. --__--*")
            exit()


if __name__ == "__main__":
    
    print("*--__-- WGUPS Postal Delivery Service --__--*","\n")
    print("""                                         
 .----------------------------------......._____       |
 |______________________________________________`_,    |
 |  .--------------..--------------.  |.----------,\   |
 |  |                              |  ||           \\  |
 |  \                              /  ||            \\ |
 |  /                              \  ||             \\|_
 |  `--------------..------------- '  ||              \\/ .---------.
 |____________________________________||_______________\\_(_________)_
 | .---.                        .---. |                `%,------------~-.
 | |(O)| WGUPS Delivery Service |(O)| |  __             |               |
(| `---'                        `---' | (- \            |               |)
(|                                    |  ~~             |               |
 |                                    |                 |               |
 |       __,---,__                    |                `%,  __,---,__   |_
=|______//       \\___________________|_________________|__//       \\__|_]
        |   .-.   |                                        |   .-.   |
        |   `-'   |                                        |   `-'   |
         \_     _/                                          \_     _/
           `---'                                              `---'""")
    main()
    wgups_UI()