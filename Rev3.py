#Harry Derouich
#27/01/15
#Records Class Exercises - Revision 3

class EmployeeDetails:
    def __init__(self):
        self.Name = None
        self.Number = None
        self.HoursWorked = None
        self.HourPay = None
        self.TotalPay = None

def initiate_record():
    pay_slip = EmployeeDetails()
    print('Pay Slip Generator')
    print('')
    pay_slip.Name = input("Please enter the name of the employee: ")
    pay_slip.Number = input("Please enter the employee's number: ")
    pay_slip.HoursWorked = input("Please enter the hours worked by this employee: ")
    pay_slip.HourPay = input("Please enter the employee's hourly rate of pay: ")
    pay_slip.TotalPay = int(pay_slip.HoursWorked) * int(pay_slip.HourPay)
    titles = ['Pay Slip: ','Name: ','Employee Number: ','Hours Worked: ','Rate of Pay: ', 'Total Pay: ']
    return pay_slip, titles

def length_validation(pay_slip):
##  longest = 30
    if len(pay_slip.Name) > 26:
        longest = len(pay_slip.Name) + 6
        return longest
    else:
        longest = 35
        return longest    
##    if len(pay_slip.Number) > 15:
##        longest = len(pay_slip.Number) + 17
##        return longest
##    if len(pay_slip.HoursWorked) > 18:
##        longest = len(pay_slip.HoursWorked) + 14
##        return longest
##    if len(pay_slip.HourPay) > 18:
##        longest = len(pay_slip.HourPay) + 13
##        return longest
##    if len(str(pay_slip.TotalPay)) > 20:
##        longest = len(str(pay_slip.TotalPay))
##        return longest
    return longest

#longest keeps getting overwritten

def generator(titles, longest, pay_slip):
    print('*' * longest)
    print('* {0:<{1}} *'.format(titles[0],longest))
    print('*'+' '*longest+'*')
    print('* {0}{1:<{2}}*'.format(titles[1],pay_slip.Name,longest))
    print('* {0}{1:<{2}}*'.format(titles[2],pay_slip.Number,longest))
    print('* {0}{1:<{2}}*'.format(titles[3],pay_slip.HoursWorked,longest))
    print('* {0}£{1:<{2}}*'.format(titles[4],pay_slip.HourPay,longest))
    print('*' + (' '* longest) + '*')
    print('* {0}£{1:<{2}}*'.format(titles[5],pay_slip.TotalPay,longest))
    print('*'*longest)

pay_slip, titles = initiate_record()
longest = length_validation(pay_slip)
print(longest)
generator(titles, longest, pay_slip)
