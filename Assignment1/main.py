from datetime import datetime
from fileinput import close
from os.path import exists
from exceptions import NullValueError, NumValueError, AlphaValueError
import csv


def get_name():
    """function to get name from user"""
    while True:
        name = input("Enter your Name: ")
        try:
            if not name:
                raise NullValueError
            else:
                return name
        except NullValueError:
            print("Name can't be empty.")


def get_age():
    """function to get age from user"""
    while True:
        age = input("Enter your Age: ")
        try:
            if not age:
                raise NullValueError
            if age.isalpha():
                raise ValueError
            age = int(age)
            return age

        except NullValueError:
            print("Age can't be empty.")
        except ValueError:
            print("Age can contain only numbers.")


def get_date():
    """function to get date from user"""
    while True:
        date = input("Date: ")
        try:
            if not date:
                raise NullValueError
            if date.isalpha():
                raise AlphaValueError
            date = datetime.strptime(date, "%Y/%m/%d")
            return datetime.strftime(date, "%Y/%m/%d")

        except NullValueError:
            print("Date can't be empty.")
        except AlphaValueError:
            print("Date must not contain alphabets.")
        except:
            print("Date must be in format YYYY/MM/DD.")


def get_hobbies():
    """function to get hobbies of user"""
    while True:
        hobbies = input("Enter your Hobbies: ")
        try:
            if not hobbies:
                raise NullValueError
            else:
                return hobbies
        except NullValueError:
            print("Hobbies can't be empty.")
        except:
            print("Please enter hobbies.")


# Function to call all input functions
def input_data():
    data = {}
    data["name"] = get_name()
    data["dob"] = get_date()
    data["age"] = get_age()
    data["hobbies"] = get_hobbies()
    return data


def saveToCSV(filename, fieldnames, data, is_new):
    """function to save a data into csv format"""
    if is_new:
        filemode = "w"
    else:
        filemode = "a+"
    with open(filename, mode=filemode) as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        if is_new:
            writer.writeheader()
        writer.writerow(data)
        csv_file.close()
        return True


def main():
    data = input_data()
    fieldnames = ["name", "dob", "age", "hobbies"]
    filename = "data.csv"
    is_new = not exists(filename)
    saveToCSV(filename, fieldnames, data, is_new)


if __name__ == "__main__":
    main()
