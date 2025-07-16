class Student:
    def __init__(self,name,roll_no,age, marks):
        self.name=name
        self.roll_no=roll_no
        self.age=age
        self.marks=marks
    def __str__(self):
        return 'name:{},roll_no:{},age:{},marks:{}'.format(self.name,self.roll_no,self.age,self.marks)
    
class Studentmanagement:
    def __init__(self):
        self.students=[]

    def add_student(self,name,roll_no,age,marks):
        self.students.append(Student(name,roll_no,age,marks))
        print('successfully student added')
    
    def display_students(self):
        if not self.students:
            print('not found')
            return
        for student in self.students:
            print(student)
    
    def search_student(self,roll_no):
        for student in self.students:
            if student.roll_no==roll_no:
                print(student)
                return
        print('student roll.no not found')

    def update_student(self,name,roll_no,age,marks):
        for student in self.students:
            if student.roll_no==roll_no:
                student.name=name
                student.age=age
                student.marks=marks
                print('student info is updated successfully')
                return
        print('student info not found')
    
    def del_student(self,roll_no):
        for student in self.students:
            if student.roll_no==roll_no:
                self.students.remove(student)
                print('successfully student is removed')
                return
        print('student not found to delete')

def main():
    sm=Studentmanagement()
    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search Student by Roll No")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")
        
        if choice=='1':
            name=input('enter student name:')
            roll_no=int(input('enter roll number:'))
            age=int(input('enter age of student:'))
            marks=int(input('enter marks scored by student:'))
            sm.add_student(name,roll_no,age,marks)
        elif choice=='2':
            sm.display_students()
        elif choice=='3':
            roll_no=int(input('enter roll.no:'))
            sm.search_student(roll_no)        
        elif choice=='4':
            roll_no=int(input('enter roll number:'))
            name=input('enter name:')
            age=int(input('enter age'))
            marks=int(input('enter marks scored:'))
            sm.update_student(name,roll_no,age,marks)

        elif choice=='5':
            roll_no=int(input('enter roll number:'))
            sm.del_student(roll_no)
        elif choice=='6':
            print('logging out')
            break
        else:
            print('enter proper choice')
        
if __name__=='__main__':
    main()