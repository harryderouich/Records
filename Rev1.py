#Harry Derouich
#23/01/15
#Records Class Exercises - Revision 1

class StudentMarks:
    def __init__(self):
        self.StudentName = None
        self.TestMark = None

new_record = StudentMarks

new_record.StudentName = input("Name: ")
new_record.TestMark = input("Mark: ")





print('{0}: {1} Marks'.format(new_record.StudentName, new_record.TestMark))


