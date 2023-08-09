"""Gather information from user to make a Person instance saved into CSV"""
import csv


class Person:
    """Person class"""

    def __init__(self, name, age, location, hobby):
        self._name = name
        self._age = age
        self._location = location
        self._hobby = hobby

    def __str__(self) -> str:
        return (
            f"Name: {self._name}, Age: {self._age}, Location:"
            f" {self._location}, Hobby: {self._hobby}"
        )

    def person_dict(self):
        """Create a dictionary object from Class instance"""
        new_person = {
            "Name": self._name,
            "Age": self._age,
            "Location": self._location,
            "Hobby": self._hobby,
        }

        return new_person


def main() -> None:
    """Main function of program"""

    information = get_input()
    person_data = get_person(information)
    store_person(person_data)


def get_input():
    """Ask user for input and check for proper number of arguments"""

    name = input("First Name: ")
    age = input("Age: ")
    location = input("Location: ")
    hobby = input("Favorite Hobby: ")

    return [name, age, location, hobby]


def get_person(info):
    """Create person instance based on information input by user"""

    person = Person(*info)
    new_person = person.person_dict()
    print(person)
    return new_person


def store_person(data):
    """Get person instance and save to CSV file"""

    with open("person.csv", "a", newline="", encoding="utf-8") as file:
        fieldnames = ["Name", "Age", "Location", "Hobby"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        if file.tell() == 0:
            writer.writeheader()

        writer.writerow(data)
        print("data processed")


if __name__ == "__main__":
    main()
