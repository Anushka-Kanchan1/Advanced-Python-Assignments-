def report_header(func):
    def wrapper(self):
        print("=" * 45)
        print("       STUDENT PERFORMANCE REPORT")
        print("=" * 45)
        func(self)
        print("=" * 45)
    return wrapper


class StudentReport:

    college = "ABC Engineering College"

    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    @classmethod
    def change_college(cls, new_college):
        cls.college = new_college

    def __str__(self):
        return "Name: " + self.name + ", Roll No: " + str(self.roll_no)

    @report_header
    def display_report(self):
        print("College :", StudentReport.college)
        print("Name    :", self.name)
        print("Roll No :", self.roll_no)
        print("Marks   :", self.marks)

        if self.marks >= 40:
            print("Result  : PASS")
        else:
            print("Result  : FAIL")


student1 = StudentReport("Rahul", 101, 85)
print(student1)
student1.display_report()

print()

StudentReport.change_college("XYZ Institute of Technology")

student2 = StudentReport("Priya", 102, 35)
print(student2)
student2.display_report()


OUTPUT

=============================================
       STUDENT PERFORMANCE REPORT
=============================================
College : ABC Engineering College
Name    : Rahul
Roll No : 101
Marks   : 85
Result  : PASS
=============================================

Name: Priya, Roll No: 102

=============================================
       STUDENT PERFORMANCE REPORT
=============================================
College : XYZ Institute of Technology
Name    : Priya
Roll No : 102
Marks   : 35
Result  : FAIL
=============================================
