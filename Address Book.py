address_book = []

def refresh_book():
    global address_book
    address_book = sorted(address_book, key=lambda person: person.name)

def display_content():
    refresh_book()
    for p in address_book:
        if(type(p).__name__ == "person"):
            print(p.name)
            print(" address:"+p.address)
            print(" number:"+p.number)
            print(" email:"+p.email)
            print("")

class person:
    def __init__(self, name,address,number,email):
        self.name = name
        self.address = address
        self.number = number
        self.email = email

    def set_name(self, name):
        self.name = name
        
    def set_address(self,address):
        self.address = address
        
    def set_number(self,number):
        self.number = number
        
    def set_email(self, email):
        self.email = email

def create_person():
    name = input('Please enter a name:')
    address = input('Please enter an address:')
    number = input('Please enter a phone number:')
    email = input('Please enter an email:')
    p = person(name,address,number,email)
    return p
    

a = person("Marquise","Chicago","1234567","Mmadjahwqxncsajaajgo@Eemail.com")
address_book.append(a)

a = person("Danial","Chicago","Unknown","Unknown")
address_book.append(a)

display_content()



