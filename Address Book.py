address_book = []

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


a = person("Marquise","Chicago","1234567","Mcago@email.com")
address_book.append(a)

for p in address_book:
    if(type(p).__name__ == "person"):
        print(p.name)
        print(" address:"+p.address)
        print(" number:"+p.number)
        print(" email:"+p.email)
        print("")
