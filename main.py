class Contacts:

    def __init__(self,First_name,Last_name,Address,State,City,Zip,Phone_number,Email):
        self.First_name = First_name
        self.Last_name = Last_name
        self.Address = Address
        self.State = State
        self.City = City
        self.Zip = Zip
        self.Phone_number = Phone_number
        self.Email = Email

class Addressbook:
    def __init__(self):
        self.contacts = []

    def add_person(self,con_obj):
        if con_obj.First_name in self.contacts:
            print("Person already present")
            return
        self.contacts.append(con_obj)
        print("Contacts Added")

    def display(self):
        for i in self.contacts:
            print("===========================")
            print("\tFirst name: {}".format(i.First_name))
            print("\tLast name: {}".format(i.Last_name))
            print("\tAddress: {}".format(i.Address))
            print("\tState: {}".format(i.State))
            print("\tCity: {}".format(i.City))
            print("\tZip: {}".format(i.Zip))
            print("\tPhone number: {}".format(i.Phone_number))
            print("\tEmail: {}".format(i.Email))

if __name__ == '__main__':

    Add = Addressbook()
    n = 0
    while n != 3:
        print("1.Add Person\n2.Display person\n3.Exit")
        n = int(input("Enter choice: "))
        if n == 1:
            f_name = input("Enter First Name: ")
            l_name = input("Enter Last Name: ")
            address = input("Enter Address: ")
            state = input("Enter State: ")
            city = input("Enter City: ")
            zip = input("Enter Zip: ")
            mob = input("Enter mob: ")
            email = input("Enter Email: ")
            con = Contacts(f_name,l_name,address,state,city,zip,mob,email)
            Add.add_person(con)
        elif n == 2:
            Add.display()
        else:
            break
