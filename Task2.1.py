#taking input of lists1
list1 = [] 

#taking the input of length of list from the user
number = int(input("Enter the length of the list: "))

#after taking user input , taking input of elements in the list 

for i in range(number):
    data = int(input("Enter the elements you want to include in the list"))
    list1.append(data)
    print (list1)

# creating a new empty list to store those new values in 
new_list= []

# now seprating negative integers from the list and printing it out

for i in list1 :
    if i > 0 :
        new_list.append(i)

print (list1)
print(new_list)
