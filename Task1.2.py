# WAP to seperate the file extension and print the file extension name

filename = input("File name: ")


#splitting the file extension from the file name 
extension = filename.split(".")[-1]

#printing the extension name 
print (extension)