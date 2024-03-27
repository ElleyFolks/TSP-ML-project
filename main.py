# RUBRIC - Section C1, Student Name: Elley Folks, Student ID: 010139574 

import datetime as dt
from package import Package
from hub import Hub
from hash_Table import hash_table
from delivery import Delivery_Truck
from user_interface import delivery_menu as menu

# PROCESS - Creating hash tables, storing data from CSVs into buckets.
package_hash_table = hash_table(length=40)
Package.import_package(package_hash_table)

hub_hash_table = hash_table(length=30)
Hub.import_hubs(hub_hash_table)

def main():

    # PROCESS - Loading packages onto trucks via package ID.
    load_1: list = [1, 13, 5, 14, 15, 16, 19, 20, 29, 30, 31, 37, 40]
    delivery_truck_1: Delivery_Truck = Delivery_Truck(load_1, truck_departure_time = dt.timedelta(hours= 8)) # leaves right at 8:00AM

    load_2: list = [2, 3, 4, 7, 8, 18, 25, 32, 34, 6, 28, 36, 38]
    delivery_truck_2: Delivery_Truck = Delivery_Truck(load_2,truck_departure_time= dt.timedelta(hours=9, minutes= 30)) # leaves when packages delayed in flight arrive

    load_3: list = [9, 10, 11, 12, 17, 21, 35, 22, 23, 24, 26, 27, 33, 39]
    delivery_truck_3 = Delivery_Truck(load_3, truck_departure_time= dt.timedelta(hours=10, minutes=30)) # leaves when truck driver is available 

    # PROCESS - Calling function to deliver packages.
    delivery_truck_1.deliver_packages(package_hash_table, hub_hash_table)
    delivery_truck_2.deliver_packages(package_hash_table, hub_hash_table)
    delivery_truck_3.deliver_packages(package_hash_table, hub_hash_table)

    # PROCESS - Sums up the combined distance traveled of each truck (must be under 140 miles).
    total_distance = delivery_truck_1.miles_traveled + delivery_truck_2.miles_traveled + delivery_truck_3.miles_traveled

    print(f"\n --*-- Total milage of all trucks: {total_distance} miles. --*--\n")
    return delivery_truck_1, delivery_truck_2, delivery_truck_3, total_distance


# FLOW - Executes main function, creates user interface to view package status and milage of trucks.
if __name__ == "__main__":
    
    print("*--__-- WGUPS Postal Delivery Service --__--*","\n")
    truck_1, truck_2, truck_3, total_milage = main()
    
    # FLOW - Creating user interface for viewing package status and total milage with specific truck objects.
    interface = menu(truck_1, truck_2, truck_3, total_milage, package_hash_table)
    interface.user_menu()
    