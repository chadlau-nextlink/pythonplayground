employee_file = open("record.txt", "r") #read
# open("xx.txt", "w") #write, will overwrite the file
# open("xx.txt", "a") #append, add record in the end of document
# open("xx.txt", "r+w")
print(employee_file.readable()) #return true or false
print(employee_file.read()) #read actual file
# print(employee_file.readline()) #read first file
# print(employee_file.readlines()[1]) #read first file
# employee_file.write("Peter Parker")
employee_file.close() #need to close file after opened