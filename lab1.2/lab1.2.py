from func import *

file_1 = "cars_1.txt"
file_2 = "cars_2.txt"

file_mode = enter_file_mode()

n = int(input("Enter the number of cars: "))

create_fist_file(file_1, n, file_mode)

print("List of cars(first file):")
output_file(file_1)

month = int(input("Enter the month number: "))

year = int(input("Enter the year: "))

create_list_recent_cars(file_1, file_2, month, year)

print(f"List of cars which started selling this month(second file): ")
output_file(file_2)

output_worn_cars(file_1)
