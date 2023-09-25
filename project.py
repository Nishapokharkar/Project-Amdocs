from validate import *
class Employee:
    EmpDict = { }
    def __init__(self,e,nm,sr,doj,a,ano,panno,address,dob,city,department,designation,gender):
        self.eid=e
        self.name=nm
        self.sal=sr
        self.str=doj
        self.age=a
        self.adno=ano
        self.pno=paano
        self.gender = gender
        self.address = address
        self.city = city
        self.dob = dob
        self.department = department
        self.designation = designation
        if self.department in self.EmpDict.keys():
            self.EmpDict[self.department].append(self.name)
        else:
            self.EmpDict[self.department] = [self.name]
    def display(self):
        print("Employee ID=",self.eid)
        print("Employee name=",self.name)
        print("Employee salary:",self.sal)
        print("Employee date of joinig:",self.str)
        print("Employee age=",self.age,)
        print("Employee adhar no is:",self.adno)
        print("Employee pan no is:",self.pno)
        print("Employee gender is:",self.gender)
        print("Employee adress is:",self.address)
        print("Employee city is:",self.city)
        print("Employee date of birth is:",self.dob)
        print("Employee departments is:",self.department)
        print("Employee designation is:",self.designation)
        
    @classmethod
    def DispEmployee(self):
        for k,v in self.EmpDict.items():
            print ("Employee details: ",k)
            for ename in v:
                print(ename,end=" ")
            print("")
        


emplist = []
print("Student Management System")
print("")
while True:

    print("Employee Management System")

    print("*********MENU**********")

    print("1.Enter the employee details")

    print("2.Enter the record to delete:")

    print("3.Display the details")

    print("4.Enter the details to update:")

    print("5.Enter the details to search:")

    print("6.Displat the details with highest salary:")

    print("7.Display teh details of Employee with highest salary:")

    print("8.EXIT")

    choice = int(input("Enter your choice "))
    if (choice == 1):
        while True:
            e = input("Enter Employee ID: ")
            if any(emp.eid == e for emp in emplist):
                print("Invalid: Employee ID already exists. Please enter a new ID.")
            elif isIdValid(e):
                break
            else:
                print("Invalid: Please enter a correct ID.")
        while True:
            nm=input("Enter the name of string:")
            if isNameValid(nm):
                break
            else:
                print("Invalid name")
        while True:
            sr=(input("enter the salary:"))
            if issalvalid(sr):
                 break
            else:
                print("Slaalry not valid")

        while True:
            a=int(input("Enter the age:"))
            if isagevalid(a):
                break
            else:
                print("Invalid  age")
        while True:
            doj=input("Enter the date of joining")
            if isDatevalid(doj):
                break
            else:
                print("Date is invalid")
        while True:
            ano=input("Enter the adhar no:")
            if isAdharvalid(ano):
                break
            else:
                print("adhar no is not valid")
        while True:
            paano=input("Enter the PAN no:")
            if isPanValid(paano):
                break
            else:
                print("Pan no is not valid")
        while True:
            gender=input("Enter the gender:")
            if isgenderValid(gender):
                break
            else:
                print("Gender is not valid")
        while True:
            dob=input("Enter the date of birth:")
            if isDatevalid(dob):
                break
            else:
                print("Date of birth is not")
        while True:
            address=input("Enter the address:")
            if isAddressValid(address):
                break
            else:
                print("adress is not valid")
        while True:
            city=input("Enter the city:")
            if isCityValid(city):
                break
            else:
                print("City is not valid")
        while True:
            department=input("Enter the departmenet:")
            if isDnameValid(department):
                break
            else:
                print("department not valid")
        while True:
            designation=input("Enter teh designamtion:")
            if isDesiValid(designation):
                break
            else:
                print("design is not valid")


        emp = Employee(e,nm,sr,doj,a,ano,paano,address,dob,city,department,designation,gender)
        emplist.append(emp)
    elif choice==2:
        while True:
            if len(emplist)<0:
                print("List is empty")
            else:
                id=input("Enter the id to be deleted")
                if(isIdValid(id)):
                    flag=0
                    for i in emplist:
                        if i.eid==id:
                            emplist.remove(i)
                            flag=1
                            break
                    if flag:
                        for k,v in Employee.EmpDict.items():
                            if i.name in v:
                                v.remove(i.name)
                        print("RECORD deleted succesfully")
                    else:
                        print("record not exist") 
                break                       

    elif choice==3:
        for i in emplist:
            i.display( )

    elif choice==4:
        print("Select the field to update:")
        print("a. Update Name")
        print("b. Update Address")
        print("c. Update DOB")
        print("d. Update Salary")
        sub_choice = input("Enter your choice: ")
        if sub_choice == 'a':
            e=(input("Enter teh employee id:"))
            for i in emplist:
                flag=1
                if i.eid==e:
                    new_name = input("Enter new Name: ")
                    i.name = new_name
                    print("Name updated sucesfully!")
                    flag=1
                    break

                else:
                    flag=0

            if flag==0:
                print("ID not found")
            
        elif sub_choice == 'b':
                e=(input("Enter teh employee id:"))
                for i in emplist:
                    if i.eid==e:
                        flag=1
                        new_address = input("Enter new Address:")
                        i.address= new_address
                        print("Address updated successfully!")
                        break
                    else:
                        flag=0
                if flag==0:
                    print("ID not found")
        elif sub_choice == 'c':
                    e=(input("Enter teh employee id:"))
                    for i in emplist:
                        if i.eid==e:
                            flag=1 
                            new_dob = input("Enter new DOB:")
                            i.dob = new_dob
                            print("Date of Birth updated successfully!")
                            break
                        else:
                            flag=0
                    if flag==0:
                        print("ID not found")

        elif sub_choice == 'd':
                    print("Select the field to update salary:")
                    print("1.Update the salary of specific Employee by Employee id.")
                    print("11.Update the salary of all Employees working in specific department.")
                    print("111.Update the salary of all Employees.")
                    ch=int(input("Enter the choice to update salary:"))
                    if (ch== 1):
                        e = input("Enter Employee ID to update salary ")
                        for i in emplist:
                            if i.eid==e:
                                flag=1
                                new_salary = (input("Enter new Salary: "))
                                i.sal=new_salary
                                print("Salary updated succesfully:")
                                break
                            else:
                                flag=0
                        if flag==0:
                            print("id doesnt exist")
                    elif (ch == 11):
                        sdname=input("Enter the specific department to update salary:")
                        if sdname in Employee.EmpDict.keys():
                            new_salary = (input("Enter new Salary: "))
                            for i in emplist:
                                flag=1
                                if i.department==sdname:
                                    i.sal = new_salary
                                    print("salary updated succesfully")
                                    break
                                else:
                                    flag=0
                        if flag==0:
                            print("invalid department name")
                    elif(ch == 111):
                        new_salary = (input("Enter new Salary: "))
                        for i in emplist:
                            i.sal=new_salary
                            print("salary updated succesfully")
                        
        else:
            print("Inavlid choice,please enter the invalid choice")
            
    elif choice == 5:
        print("")
        print("Press A to search by Employee id:")
        print("Press B to search by Employee Name:")
        print("Press C to search by Department Name:")
        ch = input("Enter your choice")
        if (ch == "A"):
            e = input("Enter the emp id  to be searched ")
            for i in emplist:
                flag=1
                if i.eid==e:
                   i.display( )
                   break
                else:
                    flag=0
            if flag==0:
                print("ID not valid")


        elif(ch == "B"):
            nm = input("Enter the Name to be searched ")
            for i in emplist:
                flag=1
                if i.name==nm:
                   i.display( )
                   break
                else:
                    flag=0
            if(flag==0):
                print("Name not valid")
        elif(ch == "C"):
            department=input("Enter the department name:")
            for i in emplist:
                flag=1
                if i.department==department:
                    i.display()
                    break
                else:
                    flag=0
            if(flag==0):
                print("department not valid")
        else:
            print("Invalid choice,Re-enter the choice")

    elif choice == 6:
        max=0
        for i in emplist:
            if int(i.sal)>max:
                max=int(i.sal)
        for i in emplist:
            if int(i.sal)==max:
                print("Employee with highest Salary is:")
                i.display()


    elif choice == 7:
        min=9999999
        for i in emplist:
            if int(i.sal) < min:
                min=int(i.sal)
        for i in emplist:
            if int(i.sal)==min:
                print("Employee with lowest Salary is:")
                i.display()
    
    elif choice == 8:
        print("EXIT")
        break

    else:
        print("Invalid choice Please Enter your choice again !!!")

