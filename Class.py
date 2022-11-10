class Employee:
    empCount = 0
    def __init__(self, Name, Email, Age):
        self.Name = Name
        self.Email = Email
        self.Age = Age
        Employee.empCount += 1
    def displayCount(self):
        print('Total Employee Number is: ' +str(Employee.empCount))
    def displayInformation(self):
        print('Name: ',self.Name, 'Email: ',self.Email, 'Age: ',self.Age)

employee1 = Employee('Adam', 'adam@gmail.com', '24')
employee2 = Employee('Joseph', 'joseph@gmail.com', '30')
employee3 = Employee('Joy', 'joy@gmail.com', '25')
employee4 = Employee('Ose', 'ose@gmail.com', '27')
employee5 = Employee('Franca', 'franca@gmail.com', '29')
