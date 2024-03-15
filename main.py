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
    print(f"*--__-- Truck total milage is {total_distance} miles. --__--*")


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
            user_time_str:str = input("        Please enter the time (24 hour HH:mm:ss) you want to see the status of all packages.")
            (entered_hrs, entered_min, entered_sec) = user_time_str.split(':')
            
            user_time = dt.timedelta(hours = int(entered_hrs), minutes= int(entered_min), seconds= int(entered_sec))

            # gets info for packages 0 - 39 (40 total)
            for i in range(1,41):
                searched_package:Package = packageHashTable.search_item(i)

                if searched_package.departureTime < user_time < searched_package.deliveryTime:
                    print("-->--> Package status - EN ROUTE -->-->")
                    print("        Package Info:", searched_package)

                elif user_time < searched_package.departureTime:
                    print("-----| Package status - AT HUB |-----")
                    print("        Package Info:", searched_package)

                else:
                    print("-->--x Package status - DELIVERED -->--x")
                    print("        Package Info:", searched_package)

        elif user_choice == '3':
            using_menu = False
            print("*--__-- Thankyou for shipping with WGUPS! Exiting program. --__--*")
            exit()


if __name__ == "__main__":
    
    print("*--__-- WGUPS Postal Delivery Service --__--*","\n")
    main()
    wgups_UI()

    

