# C950
# Created by AbdAllah M AbdAllah Khodeir
# Student ID: 010734215

import csv
import datetime


class HashMap:
    # constructor with a default capacity of 20
    def __init__(self, capacity=20):
        # the map data structure to store key-value pairs
        self.map = []
        # capacity of the hash map
        self.capacity = capacity
        # size of the hash map
        self._size = 0
        # initialize an empty list for each bucket
        # O(capacity)
        for i in range(self.capacity):
            self.map.append([])

    # insert a key-value pair into the hash map
    # Citing source: WGU code repository W-2_ChainingHashTable_zyBooks_Key-Value_CSV_Greedy.py
    # O(1) average case, O(n) worst case
    def insert(self, key, value):
        # calculate the bucket number using the hash of the key
        bucket = hash(key) % self.capacity
        # get the list of key-value pairs in the bucket
        bucket_list = self.map[bucket]
        # search for an existing key
        # O(n) average case, O(n) worst case
        for kv in bucket_list:
            # if the key already exists, update the value
            if kv[0] == key:
                kv[1] = value
                return
        # if the key does not exist, add a new key-value pair
        key_value = [key, value]
        bucket_list.append(key_value)
        self._size += 1
        # if the load factor exceeds 0.7, resize the hash map
        # O(n)
        if self._size >= 0.7 * self.capacity:
            self.resize()

    # lookup the value of a given key
    # O(1) average case, O(n) worst case
    def lookup(self, key):
        # calculate the bucket number using the hash of the key
        bucket = hash(key) % self.capacity
        # get the list of key-value pairs in the bucket
        bucket_list = self.map[bucket]
        # search for the key in the bucket
        # O(n) average case, O(n) worst case
        for i in bucket_list:
            # if the key is found, return the value
            if key == i[0]:
                return i[1]
        # if the key is not found, raise an error
        raise KeyError("Key not found in hash map")

    # remove the key-value pair of a given key
    # O(1) average case, O(n) worst case
    def remove(self, key):
        # calculate the bucket number using the hash of the key
        index = hash(key) % self.capacity
        # get the list of key-value pairs in the bucket
        destination = self.map[index]
        # search for the key in the bucket
        # O(n) average case, O(n) worst case
        for i in range(len(destination)):
            # if the key is found, delete the key-value pair
            if destination[i][0] == key:
                del destination[i]
                self._size -= 1
                return
        # if the key is not found, raise an error
        raise KeyError("Key not found in hash map")

    # resize the hash map
    # O(1) average case, O(n) worst case
    def resize(self):
        # store the old map data
        old_map = self.map
        # double the capacity of the hash map
        self.capacity = 2 * self.capacity
        # reset the size of the hash map
        self._size = 0
        # initialize a new empty map
        self.map = []
        for i in range(self.capacity):
            self.map.append([])
        # reinsert all the key-value pairs into the new map
        for bucket in old_map:
            for key_value in bucket:
                self.insert(key_value[0], key_value[1])


# Package class definition
class Package:

    # Constructor to initialize Package attributes
    # Time complexity: O(1)
    def __init__(self, id, package_address, package_city, package_state, zipcode, delivery_deadline, package_weight,
                 package_status):
        # ID of the Package
        self.id = id
        # Address of the Package recipient
        self.package_address = package_address
        # City of the Package recipient
        self.package_city = package_city
        # State of the Package recipient
        self.package_state = package_state
        # Zipcode of the Package recipient
        self.zipcode = zipcode
        # Deadline time of the Package
        self.delivery_deadline = delivery_deadline
        # Weight of the Package
        self.package_weight = package_weight
        # Status of the Package (Delivered, En route, or At Hub)
        self.package_status = package_status
        # Departure time of the Package from the Hub
        self.departure_time = None
        # Delivery time of the Package to the recipient
        self.delivery_time = None

    # Method to return a string representation of the Package object
    # Time complexity: O(1)
    def __str__(self):
        return "Package ID: {id}\nStreet Address: {package_address}\nCity: {package_city}\nState: {package_state}\n" \
               "Zip Code: {zipcode}\nDelivery Deadline: {delivery_deadline}\nPackage Weight: {package_weight}\n" \
               "Status: {package_status}\nDelivery Time: {delivery_time}\n".format(

                id=self.id,
                package_address=self.package_address,
                package_city=self.package_city,
                package_state=self.package_state,
                zipcode=self.zipcode,
                delivery_deadline=self.delivery_deadline,
                package_weight=self.package_weight,
                delivery_time=self.delivery_time,
                package_status=self.package_status
                )

    # Method to update the Package status based on delivery/departure time
    # Time complexity: O(1)
    def update_status(self, convert_timedelta):
        # If delivery time is available and less than current time, set status to "Delivered"
        if self.delivery_time and self.delivery_time < convert_timedelta:
            self.package_status = "Delivered"
        # If departure time is available and greater than current time, set status to "En route"
        elif self.departure_time and self.departure_time > convert_timedelta:
            self.package_status = "En route"
        # If neither delivery nor departure time is available or both are equal to current time, set status to "At Hub"
        else:
            self.package_status = "At Hub"


# Truck class definition
class Truck:
    def __init__(self, truck_capacity, truck_speed, truck_load, truck_packages, truck_mileage, truck_address,
                 truck_depart_time):
        self.truck_capacity = truck_capacity
        self.truck_speed = truck_speed
        self.truck_load = truck_load
        self.truck_packages = truck_packages
        self.truck_mileage = truck_mileage
        self.truck_address = truck_address
        self.truck_depart_time = truck_depart_time
        self.time = truck_depart_time

    def __str__(self):
        return "Truck Information:\n" \
               "Capacity: {}\nSpeed: {}\nLoad: {}\nPackages: {}\nMileage: {}\nAddress: {}\nDeparture Time: {}\n" \
               "Current Time: {}".format(
                    self.truck_capacity, self.truck_speed, self.truck_load, self.truck_packages, self.truck_mileage,
                    self.truck_address, self.truck_depart_time, self.time
               )
# O(1) for initializing truck instances and creating a hashmap instance


# Read the file of distance information
with open("data/Distance.csv") as file_one:
    file_distance = csv.reader(file_one)
    file_distance = list(file_distance)
# O(n) for reading the CSV_Distance where n is the number of rows

with open("data/addresses.csv") as file_two:
    file_address = csv.reader(file_two)
    file_address = list(file_address)
# O(n) for reading the CSV_Address where n is the number of rows

with open("data/packages.csv") as file_three:
    file_package = csv.reader(file_three)
    file_package = list(file_package)
# O(n) for reading the CSV_Package where n is the number of rows


def get_package(file_name, package_hash_tab):
    # loads the package information from the given file
    with open(file_name) as package_info:
        package_data = csv.reader(package_info)
        for package in package_data:
            # extracting the package information from the file
            p_id = int(package[0])  # package ID
            p_address = package[1]  # package address
            p_city = package[2]  # package city
            p_state = package[3]  # package state
            p_zipcode = package[4]  # package zipcode
            p_deadline_time = package[5]  # deadline for delivering the package
            p_weight = package[6]  # weight of the package
            p_status = "At Hub"  # status of the package, initially at hub

            # creating a Package instance with the extracted information
            pac = Package(p_id, p_address, p_city, p_state, p_zipcode, p_deadline_time, p_weight, p_status)

            # inserting the package instance in the package hash table
            package_hash_tab.insert(p_id, pac)
# O(n) for loading the package data where n is the number of packages


def get_distance(x_value, y_value):
    # returns the distance between two addresses represented by their x_value and y_value
    if x_value is None or y_value is None:
        return None
    distance = file_distance[x_value][y_value]
    if distance == '':
        distance = file_distance[y_value][x_value]

    return float(distance)


def get_address(address):
    # Loop through the addresses.csv and return the row 0 (id) if the given address is found in row 2
    for row in file_address:
        if address in row[2]:
            return int(row[0])
    # Return None if the address is not found in the CSV_Address
    return None


# Initialize truck instances
truck_one = Truck(16, 18, None, [1, 13, 14, 15, 16, 19, 20, 30, 31, 34, 37, 40], 0.0, "4001 South 700 East",
                  datetime.timedelta(hours=8))

truck_two = Truck(16, 18, None, [3, 6, 12, 17, 18, 19, 21, 22, 23, 24, 26, 27, 29, 35, 36, 38, 39], 0.0,
                  "4001 South 700 East", datetime.timedelta(hours=10, minutes=20))

truck_three = Truck(16, 18, None, [2, 4, 5, 6, 7, 8, 9, 10, 11, 25, 28, 32, 33], 0.0, "4001 South 700 East",
                    datetime.timedelta(hours=9, minutes=5))

# Initialize the package_hash_table instance
package_hash_table = HashMap()

# Load the package data from the given csv file
get_package("data/packages.csv", package_hash_table)


def package_delivery(truck):
    # Initialize the list of not_delivered packages
    not_delivered = []
    # Loop through the truck's packages and add each package to not_delivered list
    for pack_ID in truck.truck_packages:
        package = package_hash_table.lookup(pack_ID)
        not_delivered.append(package)

    # Clear the truck's packages list
    truck.truck_packages.clear()

    # Continue the loop until all packages in the not_delivered list are delivered
    while len(not_delivered) > 0:
        # Initialize the next_address and next_package with maximum and None values
        next_address = float('inf')
        next_package = None
        # Loop through the not_delivered packages
        for package in not_delivered:
            # Calculate the distance between truck's address and package's address
            distance = get_distance(get_address(truck.truck_address), get_address(package.package_address))
            # If the distance is None, continue the loop
            if distance is None:
                continue
            # If the distance is less than or equal to the next_address, update the next_address and next_package
            if distance <= next_address:
                next_address = distance
                next_package = package

        # If next_package is None, break the loop
        if next_package is None:
            break

        # Add the next_package to the truck's packages list
        truck.truck_packages.append(next_package.id)

        # Remove the next_package from the not_delivered list
        not_delivered.remove(next_package)

        # Update the truck's mileage, address, and time based on the next_package's delivery
        truck.truck_mileage += next_address

        # update the truck's address with the delivery address of the next package
        truck.truck_address = next_package.package_address

        # update the truck's delivery time by adding the time taken to travel to the next package,
        # calculated as the distance divided by the average speed of the truck (18 mph)
        truck.time += datetime.timedelta(hours=next_address / 18)

        # set the delivery time of the next package as the current time of the truck
        next_package.delivery_time = truck.time

        # set the departure time of the next package as the departure time of the truck
        next_package.departure_time = truck.truck_depart_time


# deliver packages using truck1
package_delivery(truck_one)

# deliver packages using truck2
package_delivery(truck_two)

# set the departure time of truck3 to the earliest delivery time of truck1 and truck2
truck_three.depart_time = min(truck_one.time, truck_two.time)

# deliver packages using truck3
package_delivery(truck_three)


# Main Class
class Main:

    print('-------------------------------------------------------------')
    print("Western Governors University Parcel Service (WGUPS)")
    print('-------------------------------------------------------------')
    print('Created by: AbdAllah Khodeir')
    print('-------------------------------------------------------------')

    # Initialize first_input
    first_input = None

    # Loop until user inputs "Quit"
    while first_input != "Quit":
        # Print the total mileage of the three trucks
        print(f"\nThe current route mileage is: {truck_one.truck_mileage + truck_two.truck_mileage + truck_three.truck_mileage} miles.\n")  # O(1)

        # Ask the user to enter time
        first_input = input(
            'Please enter the time in format HH:MM:SS to check the status or type "Quit" to exit:\n')  # O(1)

        # If the user inputs "Quit", break the loop
        if first_input == "Quit":  # O(1)
            break

        # Try to split the user_time into hours, minutes, and seconds
        try:
            (h, m, s) = first_input.split(":")  # O(1)
            convert_timedelta = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))  # O(1)

            # Ask the user to input either "ID" or "All"
            second_input = input("To view the status of an individual package, enter 'ID'. To view a rundown of all"
                                 " packages, type 'All':\n")  # O(1)

            # If the user inputs "ID", ask for the package ID and update the status of the package
            if second_input == "ID":  # O(1)
                try:
                    package_id = input("Enter the numeric ID of the package:\n")  # O(1)
                    package = package_hash_table.lookup(int(package_id))  # O(1) on average, O(n) in worst case
                    package.update_status(convert_timedelta)  # O(1)
                    print(str(package))  # O(1)
                except ValueError:
                    print("Invalid input. Exiting program.")
                    exit()

            # If the user inputs "All", update the status of all packages
            elif second_input == "All":  # O(1)
                try:
                    for package_id in range(1, 41):  # O(n)
                        package = package_hash_table.lookup(package_id)  # O(1) on average, O(n) in worst case
                        package.update_status(convert_timedelta)  # O(1)
                        print(str(package))  # O(1)
                except ValueError:
                    print("Invalid input. Exiting program.")
                    exit()

            # Exit the program if the user inputs anything other than "ID" or "All"
            else:  # O(1)
                exit()

        # Catch ValueError if the user inputs invalid time
        except ValueError:
            print("Invalid input. Exiting program.")
            exit()

    # Print message when the program exits
    print("Exiting program. Goodbye!")  # O(1)
