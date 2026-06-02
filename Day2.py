#Email registration 
first_name=input("Enter your first name:")
last_name=input("Enter your last name:")
username=input("Enter your user name:")
password=input("Enter your password:")
confirm_password=input("Confirm your password:")
dob=input("Enter your DOB:")
recorvery_email=input("Enter your recorvery email:")
phone=int(input("Enter your phone number:"))


#Hospital booking
name=input("Enter the patient name:")
age=int(input("Ente the age:"))
disease=input("Enter the reason:")
phone=int(input("Enter phone number:"))
room_no=int(input("Enter phone number:"))


#Seat booking
name=input("Enter your name:")
phone=int(input("Enter phone number:"))
no_of_person=int(input("Enter number of person:"))
timing=input("Enter your timing:")
seat_no=int(input("Enter seat number you wish:"))


def add(a,b):
  return a+b
a=int(input("Enter number 1:"))
b=int(input("Enter number 2:"))
print(add(a,b))
