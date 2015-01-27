#Harry Derouich
#27/01/15
#Records Class Exercises - Revision 3

class EmployeeDetails:
    def __init__(self):
        self.Name = None
        self.Number = None
        self.HoursWorked = None
        self.HourPay = None

pay_slip = EmployeeDetails()
pay_slip.Name = input("Please enter the name of the employee: ")
pay_slip.Number = input("Please enter the employee's number: ")
pay_slip.HoursWorked = input("Please enter the hours worked by this employee: ")
pay_slip.HourPay = input("Please enter the employee's hourly rate of pay: ")

print('*'*30)
print('*{0:<20}')
