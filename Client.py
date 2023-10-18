
class Client:
    def __init__(self, client_id, name, email, address, phone_number, gender):
        self.client_id = int(client_id)
        self.name = name
        self.email = self.mail(email)
        self.address = address
        if len(str(phone_number)) == 10:
            self.phone_number = phone_number
        else:
            self.phone_number = '0543030304'
        if gender == 'M' or 'F':
            self.gender = gender
        else:
            self.gender = 'M'

    def mail(self,email):
        if '@' and '.com' in email:
            return email
        return 'daniel@gmail.com'

    def print_me(self):
        print(f'Client_ID:{self.client_id},Name:{self.name},Email:{self.email},Address:{self.address},Phone number:{self.phone_number},Gender:{self.gender}')

    def __str__(self):
        return f'{self.client_id}, {self.name}, {self.email}, {self.address}, {self.phone_number}, {self.gender}'

    def __repr__(self):
        return str(self)



# c1=Client(12312,'daniel','daniel@fakgmail','Tal aviv','0546666666665454545','r')
# c1.print_me()
# c2 = Client(123,"matan", "matan@gmail.com","tal aviv", 5675675678,"F")
# c2.print_me()
