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
        self.contacts.append(con_obj)

    def display(self):
        for i in self.contacts:
            print("First name: {}".format(i.First_name))
            print("Last name: {}".format(i.Last_name))
            print("Address: {}".format(i.Address))
            print("State: {}".format(i.State))
            print("City: {}".format(i.City))
            print("Zip: {}".format(i.Zip))
            print("Phone number: {}".format(i.Phone_number))
            print("Email: {}".format(i.Email))

if __name__ == '__main__':

    con = Contacts("Ashish","Patil","Sangli","MH","Sangli",416416,9156524636,"abc@gmail.com")
    Add = Addressbook()
    Add.add_person(con)
    Add.display()
