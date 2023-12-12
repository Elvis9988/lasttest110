# Author: Elvis Tamrakar, Student Id: 23056848
# By submitting this work, I assert that it is my own work and not copied from someone else or from some other source. 
# Copied work will be assigned a grade of 0 and be subject to further academic penalties at the discretion of the College.
def menu():
    print("WELCOME TO THE GRANN'S PHONE DIRECTORY")
    print("1. Add a record") 
    print("2. Search a record") 
    print("3. Update a record")
    print("4. Sort the record alphabetically")
    print("5. Delete a record")
    print("6. Quit")
    userinput= int(input("Enter your choice: "))
    return userinput
userinput = menu()
phoneDirectory={}

while userinput!=6 and userinput<6 and userinput>0:
    
    if userinput==1:
            username = str(input("Enter name: "))
            usernumber = str(input("Enter your 10-digit phone number: "))
            if not username.isalpha():
                print("Only alphabets are allowed for name")
                userinput = menu()
            elif not usernumber.isnumeric():
                print("Only numbers are allowed for number")
                userinput = menu()
            elif len(usernumber) != 10:
                print("The phone number must be exactly 10 digits, please try again")
                userinput = menu()
            else:
                phoneDirectory.update({username: {"phonenumber": usernumber}})
                print(phoneDirectory)
                userinput = menu()
                
    elif userinput==2:
        search = str(input("Enter name to search: "))
        if search in phoneDirectory:
            print (phoneDirectory.get(search))
            userinput = menu()
        else:
            print ("The name does not exist in the directory")
            userinput = menu()
            
    elif userinput==3:
        nameupdate = str(input("Enter the name for the phone number you want to update: "))
        numberupdate = str(input("Enter new 10-digit phone number: "))
        if (len(numberupdate)) > 10:
            print("The phone number cannot be more than 10 digits, please try again")
        else:
            if nameupdate in phoneDirectory:
                phoneDirectory[nameupdate] = {"phonenumber": numberupdate}                
                print("Record updated")
            else:
                print("record not found")
        userinput = menu()
        
    elif userinput==4:
        sorteddictinoary = dict(sorted(phoneDirectory.items()))
        print ("Sorted Record is: ", sorteddictinoary)
        userinput = menu()
    
    elif userinput==5:
        delete = str(input("Enter the name record you would like to delete: "))
        if delete in phoneDirectory.keys():
                phoneDirectory.pop(delete)
                print ("Record deleted")
                userinput =menu()
        else:
            print ("Name not found in directory, try again")
            userinput =menu()

else:
    pass

