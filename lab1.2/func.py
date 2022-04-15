import pickle

class Car:
    def __init__(self, name: str, release_date: str, sell_date: str):
        self.name = name
        self.release_date = release_date
        self.sell_date = sell_date

    def __str__(self):
        info = f"Car name: {self.name}, release date: {self.release_date}, sell start date: {self.sell_date}"
        return info


def enter_file_mode():
    file_mode = input("Do you want to overwrite the file or append input to it? Enter w or a: ")
    while file_mode != "w" and file_mode != "a":
        print("Incorrect input. Enter 'w' or 'a'.")
        file_mode = input("Do you want to overwrite the file or append input to it? Enter w or a: ")
    return file_mode


def create_fist_file(file_name: str, n: int, mode: str):
    if mode == "w":
        file_mode = "wb"
    else:
        file_mode = "ab"
    car_list = list()
    for i in range(n):
        print(f"Car {i+1}:")
        name = input("Enter the name of the car: ")
        release_date = input("Enter the date when this car was released in such format MM.YYYY: ")
        sell_date = input("Enter the sale start date in such format MM.YYYY: ")
        car = Car(name, release_date, sell_date)
        car_list.append(car)
    with open(file_name, file_mode) as file:
        pickle.dump(car_list, file)


def create_list_recent_cars(file_name_1: str, file_name_2: str, current_month: int, current_year: int):
    with open(file_name_1, "rb") as file:
        car_list = pickle.load(file)
    recent_cars = list()
    for car in car_list:
        month_year = car.sell_date.split(".")
        sell_month = int(month_year[0])
        sell_year = int(month_year[1])
        if sell_month == current_month and sell_year == current_year:
            recent_cars.append(car)
    with open(file_name_2, "wb") as file:
        pickle.dump(recent_cars, file)


def output_worn_cars(file_name: str):
    with open(file_name, "rb") as file:
        car_list = pickle.load(file)
    worn_cars = list()
    for car in car_list:
        month_year_sell = car.sell_date.split(".")
        sell_month = int(month_year_sell[0])
        sell_year = int(month_year_sell[1])
        month_year_release = car.release_date.split(".")
        release_month = int(month_year_release[0])
        release_year = int(month_year_release[1])
        delta_year = sell_year - release_year
        delta_month = sell_month - release_month
        if delta_year > 1 or (delta_month > 0 and delta_year == 1):
            worn_cars.append(car)
    print("Worn cars(more than one year):")
    print("-" * 70)
    for car in worn_cars:
        print(car)
    print("-" * 70)


def output_file(file_name: str):
    with open(file_name, "rb") as file:
        car_list = pickle.load(file)
    print("-" * 70)
    for car in car_list:
        print(car)
    print("-" * 70)
