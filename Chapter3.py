# Basic strings

'''
a = 34
b = "ABC"
print(a, b)
'''

# Slicing in strings

'''greeting = "Hello world, "
name = "I am ABC"
c = greeting + name
print (c)'''

# name = "Himanshu"
'''print(name[1])
print(name[0:4]) #when starting from front
print(name[-3:-1]) # when starting from back'''

# print(name[1:6:2]) #last is for spacing ie 2(1) in this case

# a = "HimanshuSinghAppleaday"
# print(a[0:8:2])
# story = "once upon a time there was a guy known to be a magician"
# print (len(story))


# String functions

'''
a = "an apple a day keeps the doctor away"
print(len(a))
print(a.endswith("doctor away"))
print(a.count("e"))
print(a.find("an")) # tells about number at which it is present
print(a.replace("apple", "orange"))
'''

# Practicing the strings

'''a = input("Please enter ypur name!!\n")
print("Good afternoon, " + a)'''

'''letter = '''# Dear <|Name|>,
# You are selected

# Date: <|Date|>
'''
name = input("Enter your name\n")
date = input("Enter date\n")
letter = letter.replace("<|Name|>", name)
letter = letter.replace("<|Date|>", date)
print(letter)'''


'''a = "this is a string with two  double  Spaces"
X = a.replace("  ", " ")
print (X)'''


