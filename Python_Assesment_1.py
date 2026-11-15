#Task 1
#Storing the values in a variables
name = "Aravindh"
age = 27
current_company = "Ascendion"
designation = "senior Quality Engineer"
learning_goal = "AI Engineer"
#Printing those values
print("My name is",name)
print("I am",age,"years old")
print("I am working in",current_company,"as a",designation,"...!")
print("My learning goal is",learning_goal)
#End of Task 1
#Task 2
num_1 = 25
num_2 = 10
#Printing all the arithmetic operations
print("The addition of two numbers is",num_1+num_2)
print("The subtraction of two numbers is",num_1-num_2)
print("The Multiplication of two numbers is",num_1*num_2)
print("The division of two numbers is",num_1/num_2)
print("The modulus of two numbers is",num_1%num_2)
print("The floor division of two numbers is",num_1//num_2)
print("The exponentiation of two numbers is",num_1**num_2)
#End of Task 2
#Task 3
#Getting the values for Task 3
student_name=input("Enter your name : ")
student_age = int(input("Enter your age : "))
student_maths_mark = int(input("Enter your Maths mark : "))
student_science_mark = int(input("Enter your Science mark : "))
student_english_mark = int(input("Enter your English mark : "))
total_marks = student_maths_mark+student_science_mark+student_english_mark
average = (student_maths_mark+student_science_mark+student_english_mark)/3
#Print the values of task 3
print("The student name is",student_name)
print("The student age is",student_age)
print("The total marks is",total_marks)
print("The average marks is",average)
print(type(student_name))
print(type(student_age))
print(type(student_maths_mark))
print(type(student_science_mark))
print(type(student_english_mark))
print(type(total_marks))
print(type(average))
#End of Task 3
#Getting the values for Task 4
value_1 = input("Enter the value 1 : ")
value_2 = input("Enter the value 2 : ")
converted_Val_1 =int(value_1)
converted_Val_2 = int(value_2)
add = converted_Val_1+converted_Val_2
mul = converted_Val_1*converted_Val_2
#Printing the values for Task 4
print(type(value_1))
print(type(value_2))
print(type(converted_Val_1))
print(type(converted_Val_2))
print("The addition of two values is",add,"and the data type is",type(add))
print("The multiplication of two values is",mul,"and the data type is",type(mul))
#End of Task 4
#Getting the values for Task 5
basic_salary = int(input("Enter the basic salary : "))
hra = int(input("Enter the HRA amount : "))
allowance = int(input("Enter the allowance amount : "))
deduction = int(input("Enter the deduction amount : "))
gross_salary = basic_salary+hra+allowance
print("Your gross salary is :",gross_salary)
net_salary = gross_salary-deduction
print("Your net salary is :",net_salary)
annual_net_salary = (gross_salary*12)-(deduction*12)
print("Your annual net salary is :",annual_net_salary)
monthly_salary = net_salary-(10/100)
print("Your monthly salary is :",monthly_salary)
#printing all the salary details
#Task 6
emp_age = int(input("Enter your age : "))
emp_exp = int(input("Enter your years of experience : "))
emp_tech_score = int(input("Enter your technnical score : "))
if(emp_age>=21):
    if(emp_exp>=2):
        if(emp_tech_score>=60):
            print("You are eligible...!")
        else:
            print("Your technical score is lesser than 60 so yopuare not eligible")
    else:
        print("Your experience is lesser than 2 years so you are not eligible")
else:
    print("Your age is lesser than 21 so you are not eligible")
#End of Task 6
#Task 7 - Identify the number is odd or even
number  = int(input("Enter the value : "))
if(number % 2 == 0):
    print("The given number is Even number")
else:
    print("The given number is Odd number")
#End of Task 7
#Task 8 - Grade identifier
student_mark = int(input("Enter the mark : "))
if(student_mark<=100):
    if(student_mark>=90):
        print("A grade")
    elif(student_mark>=80 and student_mark<=89):
        print("B grade")
    elif(student_mark>=70 and student_mark<=79):
        print("C grade")
    elif(student_mark>=60 and student_mark<=69):
        print("D grade")
    elif(student_mark>=40 and student_mark<=59):
        print("E grade")
    else:
        print("Fail")
else:
    print("Please Enter the valid number")
#End of Task 8
#Task 9 - Largest of 3 numbers
number_1 = int(input("Enter the number 1 : "))
number_2 = int(input("Enter the number 2 : "))
number_3 = int(input("Enter the number 3 : "))
if(number_1 > number_2 and number_1 > number_3):
    print("Number 1",number_1,"is bigger")
elif(number_2 > number_1 and number_2 > number_3):
    print("Number 2",number_2,"is bigger")
else:
    print("Number 3",number_3,"is bigger")
#End of task 9
#Task 10 - Calculate the electricity bill
unit = int(input("Enter the number of units : "))
first = unit-100
cal_x = unit-first
rate_1 = cal_x * 2
second = first - 100
cal_y = first - second
rate_2 = cal_y * 3
third = second - 100
cal_z = second - third 
rate_3 = cal_z * 5
default = third
rate_4 = default * 7
total_rate = rate_1 + rate_2 + rate_3 + rate_4
print("The total rate for the given unit",unit,"is : ",total_rate)
#End of Task 10