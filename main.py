import csv
import json


class Contacts:
    def __init__(self, first_name, last_name, address, state, city, zip, phone_number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.state = state
        self.city = city
        self.zip = zip
        self.phone_number = phone_number
        self.email = email

    def to_dict(self):
        try:
            return {'first_name': self.first_name}
        except Exception as ex:
            print(ex)


class Addressbook:
    def __init__(self, book_name):
        self.people = {}
        self.book_name = book_name

    def add_person(self, con_obj):
        try:
            if con_obj.first_name in self.people:
                print("Person already present")
                return
            self.people.update({con_obj.first_name: con_obj})
            print("person Added")
        except Exception as ex:
            print(ex)

    def display(self):
        try:
            for i in self.people.values():
                print("===========================")
                print("\tFirst name: {}".format(i.first_name))
                print("\tLast name: {}".format(i.last_name))
                print("\taddress: {}".format(i.address))
                print("\tstate: {}".format(i.state))
                print("\tcity: {}".format(i.city))
                print("\tzip: {}".format(i.zip))
                print("\tPhone number: {}".format(i.phone_number))
                print("\temail: {}".format(i.email))
        except Exception as ex:
            print(ex)

    def update(self, con_obj):
        try:
            if con_obj.first_name not in self.people:
                print("Person is not present")
                return
            self.people.update({con_obj.first_name: con_obj})
            print("Person updated")
        except Exception as ex:
            print(ex)

    def delete(self, name):
        try:
            for i in self.people.values():
                if name != i.first_name:
                    print("Person not present")
                    return
                del self.people[name]
                print("Person removed")
        except Exception as ex:
            print(ex)


class MultipleAddressbook:
    def __init__(self):
        self.multi_book = {}
        self.dict = {}

    def add_multi(self, address_obj):
        try:
            self.multi_book.update({address_obj.book_name: address_obj})
            print("AddressBook added")
        except Exception as ex:
            print(ex)

    def get_addressbook(self, book_name):
        return self.multi_book.get(book_name)

    def display_addressbook(self):
        try:
            for k, v in self.multi_book.items():
                for i in v.people.values():
                    print(k, "=", i.first_name, i.last_name, i.address, i.city, i.zip, i.state, i.phone_number, i.email)
        except Exception as ex:
            print("pro")
            print(ex)

    def delete_book(self, book_name):
        try:
            if book_name not in self.multi_book.keys():
                print("book is not present")
                return
            del self.multi_book[book_name]
            print("AddressBook deleted")
        except Exception as ex:
            print(ex)

    def addtoCSV(self):
        try:
            with open('addressBook.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(self.multi_book.keys())
                for v in self.multi_book.values():
                    writer.writerow(v.people.keys())
        except Exception as ex:
            print(ex)

    def addtojson(self):
        try:
            filename = 'Sample.json'
            for k, v in self.multi_book.items():
                for c in v.people.items():
                    if k not in self.dict:
                        for i in range(1):
                            self.dict.update({k: c[1].to_dict()})
            print(self.dict)
            with open(filename, 'w') as file:
                json.dump(self.dict, file, indent=4)
        except Exception as ex:
            print(ex)

    def read_csv(self):
        try:
            with open('AddressBook.csv', newline='') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
                for row in spamreader:
                    print(', '.join(row))
        except Exception as ex:
            print(ex)

    def read_json(self):
        try:
            filename = 'Sample.json'
            with open(filename, 'r') as file:
                print(json.load(file))
        except Exception as ex:
            print(ex)


def add_book():
    try:
        book_name = input("Enter Book Name: ")
        book = multi_addressbook.get_addressbook(book_name)
        if book is None:
            book = Addressbook(book_name)
        person_name = input("Enter First Name: ")
        l_name = input("Enter Last Name: ")
        address = input("Enter address: ")
        state = input("Enter state: ")
        city = input("Enter city: ")
        zip = input("Enter zip: ")
        mob = input("Enter mob: ")
        email = input("Enter email: ")
        con = Contacts(person_name, l_name, address, state, city, zip, mob, email)
        book.add_person(con)
        multi_addressbook.add_multi(book)
    except Exception as ex:
        print(ex)


def display():
    try:
        multi_addressbook.display_addressbook()
    except Exception as ex:
        print(ex)


def update_book():
    try:
        book_name = input("Enter Book Name: ")
        person_name = input("Enter name to update: ")
        book = multi_addressbook.get_addressbook(book_name)
        if book_name in multi_addressbook.multi_book.keys():
            print('present')
            for v in multi_addressbook.multi_book.values():
                for i, j in v.people.items():
                    if person_name == i:
                        l_name = input("Enter Last Name: ")
                        address = input("Enter address: ")
                        state = input("Enter state: ")
                        city = input("Enter city: ")
                        zip = input("Enter zip: ")
                        mob = input("Enter mob: ")
                        email = input("Enter email: ")
                        con = Contacts(person_name, l_name, address, state, city, zip, mob, email)
                        book.update(con)
    except Exception as ex:
        print(ex)


def delete_book():
    try:
        name = input("Enter name to update: ")
        multi_addressbook.delete_book(name)
    except Exception as ex:
        print(ex)


def add_csv():
    try:
        multi_addressbook.addtoCSV()
    except Exception as ex:
        print(ex)


def add_json():
    try:
        multi_addressbook.addtojson()
    except Exception as ex:
        print(ex)


def read_csv():
    multi_addressbook.read_csv()


def read_json():
    multi_addressbook.read_json()


if __name__ == '__main__':
    multi_addressbook = MultipleAddressbook()
    while True:
        print("1. Add Person\n2. Display person\n3. Update Person\n4. Delete\n5. Save to csv"
              "\n6. save to json\n7. read csv\n8. read json\n9. Exit")
        n = int(input("Enter choice: "))

        if n == 0:
            break
        choice = {1: add_book, 2: display, 3: update_book, 4: delete_book, 5: add_csv,
                  6: add_json, 7: read_csv, 8: read_json}
        choice.get(n)()
