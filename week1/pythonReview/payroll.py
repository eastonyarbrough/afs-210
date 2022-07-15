class Employee:
    def __init__(self, id, firstname, lastname, hourlypay):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.hourlypay = hourlypay

    def setFirstName(self, firstname):
        self.firstname = firstname

    def getFirstName(self):
        return self.firstname

    def setLastName(self, lastname):
        self.lastname = lastname

    def getLastName(self):
        return self.lastname

    def setID(self, id):
        self.id = id

    def getID(self):
        return self.id

    def setHourlyPay(self, hourlypay):
        self.hourlypay = hourlypay

    def getHourlyPay(self):
        return self.hourlypay

    def pay(self, hours):
        if float(hours) <= 40:
            total_pay = int(hours) * int(self.hourlypay)
            print('-------------------------------------------------')
            print(f'Name: {self.firstname} {self.lastname}')
            print(f'Employee ID: {self.id}')
            print('-------------------------------------------------')
            print(f'Check Balance: ${total_pay}')
            print('-------------------------------------------------')

        elif float(hours) > 40:
            overtime_pay = float(((int(hours) - 40) * (int(self.hourlypay) * 1.5)) + (40 * int(self.hourlypay)))
            print('-------------------------------------------------')
            print(f'Name: {self.firstname} {self.lastname}')
            print(f'Employee ID: {self.id}')
            print('-------------------------------------------------')
            print(f"Check Balance (w/ Overtime): ${overtime_pay:.2f}")
            print('-------------------------------------------------')

new_employee = Employee(input('Please enter employee ID: '),
    input('Please enter employee first name: '),
    input('Please enter employee last name: '),
    float(input('Please enter employee hourly rate: ')))

new_employee.pay(input(f"Enter {new_employee.firstname}'s hours worked: "))