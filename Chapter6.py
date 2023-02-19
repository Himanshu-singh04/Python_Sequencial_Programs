# Conditional expressions

'''a = 45
if(a>48):
    print("the value of a is greater than 3")
elif(a>7):
    print("the value of a is greater than 7")
else:
    print("the value is not greater than 3 and 7")'''


'''
age = int(input("Enter your age\n"))
if age>=18:
    print("you are eligible")
else:
    print("you are not eligible")
'''

# in and is operators

'''a = "apple"
if (a is "apple"):
    print("yes")
else:
    print("no")


a =[45, 9, 12]
print(15 in a)
'''

# logical operators

'''
age = int(input("Enter your age:\n"))
if (age>=18 and age<=45):
    print("you are eligible")
else:
    print("you are not eligible")
'''

# practice problems

'''

*********** GREATEST NUMBER PROGRAM ************

a = int(input("Number 1\n"))
b = int(input("Number 2\n"))
c = int(input("Number 3\n"))
d = int(input("Number 4\n"))

if (a>d):
    w1 = a
else :
    w1 = d

if(b>c):
    w2 = b
else:
    w2 = c

if (w1>w2):
    print("its the greatest", w1)
else:
    print("its the grestest", w2)

*********** PASS FAIL PROGRAM *************

sub1 = int(input("enter subject 1 marks\n"))
sub2 = int(input("enter subject 2 marks\n"))
sub3 = int(input("enter subject 3 marks\n"))

if (sub1<33 or sub2<33 or sub3<33):
    print("you are fail")
elif (sub1+sub2+sub3)/3 <40:
    print("you are fail")
else:
    print("you are passed")
'''