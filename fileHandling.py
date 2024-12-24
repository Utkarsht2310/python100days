#READING A FILE:-
# f = open('temp.txt','r') this open file with name "temp.txt"
# text = f.read() , the "text" variable contains the texts inside of the file
# print(text)
# f.close()


# WRITING A FILE:
# f = open('temp.txt2','w')
# f.write('Hello  y name is utkarsh')
# f.close()


# ADDING CONTENT IN THE FILE WITHOUT OVERWRITING IT
# f = open('temp.txt2','a') ; it appends the text into existing text.
# f.write('I am from mirzapur')
# f.close()


# USING "WITH" TO WRITE THE FILE:-
# with open('temp.txt2', 'a') as f:
#     f.write(" Hey this is with keyword!")


# READING ANY FILE LINE  BY LINE:-
# f = open('temp.txt','r')
# while True:
#     line = f.readline()
#     if not line:
#         break
#     print(line)


# FILE HANDLING FUNCTONS:-
# 1. SEEK() : - This function allows you to move current position into the file. Like if you want to  read or appennd after particular text than you can move there
# with open('temp.txt2','r') as f:
#     print(type(f))
#
#     #move to the 10th byte in the file
#     f.seek(10)
#     data = f.read(5)
#     print(data)

# 2. tell() :- This function returns the current position within the file in bytes. Useful for keeping tracks of your location into file.
# with open('temp.txt2','r') as f:
#     print(type(f))
#
#     #move to the 10th byte in the file
#     f.seek(10)
#     print(f.tell()) ; it will return "10"
#     data = f.read(5)
#     print(data)

# 3. truncate():- You can specify the size of bytes you want to store.
# with open('sample.txt', 'w') as f:
#     f.write('Hello World1')
#     #want to store only 5 characters
#     f.truncate(5)
#
# with open('sample.txt','r') as f:
#     print(f.read()) #gives only 5 char of the text as "Hello"