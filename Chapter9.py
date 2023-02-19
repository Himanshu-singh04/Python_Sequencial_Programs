# data mining

'''content = True
i = 1
with open('C:\Python\Chapter 9\sample.txt') as f :
    while content :
        content = f.readline()
        if "python" in content.lower():
            print(content)
            print(f"yes python is present {i}")
        i=i+1'''

# reading a txt file

'''apple = open('C:\Python\Chapter 9\sample.txt')
data = apple.read()
print(data)
apple.close()'''

# read line by line

'''f = open('C:\Python\Chapter 9\sample.txt')
data = f.readline()
print(data)
data = f.readline()
print(data)
f.close()'''

# with statement

'''with open('C:\Python\Chapter 9\sample.txt', 'r') as f:
    a = f.read()
print(a)'''

# write statement 

'''f = open('C:\Python\Chapter 9\sample.txt', 'a')
f.write("\nPlease write this to the file")
f.close()'''