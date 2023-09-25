import re

def isIdValid(eid):

    if eid.isdigit():

        return True

    else:

        return False

       

 
def isNameValid(name):

    l=name.split()

    if len(l)!=3:

        return False

    for i in l:

        if  i.isalpha() and i.istitle():

             return True

    return False


   

 

def issalvalid(sal):

    if sal.isdigit() and len(sal)>0:
            
            return True

    else:

            return False


 

def isagevalid(age):

    if age>=18:

        return True

    else:

        return False



def isDatevalid(doj):
    if len(doj) != 10:
        return False
    day, month, year = doj.split('/')

    if not (day.isdigit() and month.isdigit() and year.isdigit()):
        return False

    day = int(day)
    month = int(month)
    year = int(year)
    if not (1900 <= year <= 9999):
        return False

    if not (1 <= month <= 12):
        return False
    day_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and (year % 4 == 0 ):
        day_month[2] = 29  # Leap year
    if not (1 <= day <= day_month[month]):
        return False

    return True

def isDatevalid(dob):

    if len(dob) != 10:
        return False
    day, month, year = dob.split('/')

    if not (day.isdigit() and month.isdigit() and year.isdigit()):
        return False

    day = int(day)
    month = int(month)
    year = int(year)
    
    if not (1900 <= year <= 9999):
        return False
    if not (1 <= month <= 12):
        return False
    day_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and (year % 4 == 0 ):
        day_month[2] = 29  
    if not (1 <= day <= day_month[month]):
        return False

    return True



def isAdharvalid(adno):

    if adno.isdigit():

        if len(adno)==12:

             return True

        else:

            return False


 

def isPanValid(pno):

    if len(pno)==10:

        s1=pno[0:4]
        s2=pno[5:9]

        s3=pno[9]

        if  s1.isalpha() and s1.isupper() and s2.isdigit() and s3.isalpha() and s3.isupper():

            return True

        else:
            print("invalid Pan no")
            return False
        

    else:
        return False

def isgenderValid(gender):
    genders = ["Male", "Female", "Other"]

    if gender in genders:
        return True
    else:
        return False

def isAddressValid(address):
    if address.isalnum() and len(address.split())>0:
        return True
    else:
        return False

def isCityValid(city):
    if city.isalpha() and len(city)>0:
        return True
    else:
        return False

def isDnameValid(department):
    if department.isalpha() and len(department.split())>0:
        return True
    else:
        return False

def isDesiValid(designation):
    if designation.isalpha() and len(designation.split())>0:
        return True
    else:
        return False


