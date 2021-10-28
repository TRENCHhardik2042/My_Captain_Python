# School Administration project 

#csv filehandeling 
import csv

def write_in_csv(filename):
    with open('Student-Data', 'a', newline ='') as csv_file:
        writer = csv.writer(csv_file)
        
        if csv_file.tell() == 0:
            writer.writerow(["Name", "Age","Blood Group","Contact Nos.","Email ID"])
        
        writer.writerow(filename)


#condition is given for loop to run 
if __name__ == "__main__":
    condition = True 
    while (condition):
        student_data = input('Student information in the following order: (Name Age Blood-Group Contact-Number E-mail_ID) ')
        
        #Splitting the student data 
        student_data_list = student_data.split(' ')
        
        print ("Entered Student information is :\nName: {}\nAge: {}\nBlood Group: {}\nContact Nos: {}\nEmail Id: {}".format(student_data_list[0], student_data_list[1], student_data_list[2], student_data_list[3], student_data_list[4]))        
        
        # Creating a loop for verification of the input data whether to print or not
        choice_check = input("Do you want to modify the entered data (yes/no)?\n")
        
        if choice_check == 'no' :
            #Calling the csv function to append student data 
            write_in_csv(student_data_list)
            
            
            condition_check = input("For entering more data enter (yes/no)"'\n')
            
            
            # Conditioon check will be changed based on the repsone and the loop will also be decided whether to run or not 
            if condition_check == 'yes':
                condition = True
            elif condition_check == 'no':
                condition = False
        elif choice_check == 'yes':
            print ("Please re-enter the Data you Desire!")
