# for loop example

'''
a  = ["apple", "watermelon", "banana"]
for apple in a:
    print(apple)
'''

# while loop example 

'''
i = 0
a = ["apple", "banana"]
while i<len((a)):
    print(a[i])
    i = i+1
'''

# examples

'''
num = int(input("enter a number"))
for i in range(1, 11):
    print(str(num) + "X" + str(i) + "=" + str(i*num))


l1 = ["a", "b", "c"]
for name in l1:
    if name.startswith("b"):
        print("hello" + name)

num = int(input("enter the number : "))
prime = True
for i in range(2,num):
    if (num%i == 0):
        prime = False
        break
if prime:
    print("the number is prime")
else:
    print("not prime")
'''

