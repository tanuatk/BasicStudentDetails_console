#Validate username and password
def checkUserPass(username,password):
    file=open("C:\\Users\\HP\\Desktop\project\\A.txt","r")
    lines=file.readlines()
    result=False
    for line in lines:
        if username in line and password in line:
            result= True
            break       
    return result
'''-----------------------------------------------------------------------------------------'''
def continueOrExit():
    print("Do you want to continue?")
    option=str(input(" Y/N ")).lower()
    if 'y' == option:
        option=operationsOption()
        process(option)
    elif 'n'==option:
        print("Thank you")
    else:
        print("Please provide correct input.")
        continueOrExit()
'''------------------------------------------------------------------------------------'''

#Take option from admin to perform any operation 
def operationsOption():
    print(" ")
    print("Please provide any one input option to perform respective operation:")
    print("1. Get student Detais")
    print("2. Create student")
    print("3. Update student")
    print("4. Delete student")
    print("5. Log out")
    try:
        userInput= int(input("Please enter your option: "))
    except:
        print("You have entered wrong option, Please try again with correct one.")
        operationsOption()
    return userInput
'''-----------------------------------------------------------------------------------------'''

#function to Create User
def createStudent():
        print(" ")
        print("             PROGNOZ TECHNOLOGIES PVT LTD Pvt                   ")
        print("                   ADMISSION  ENQUIRY FORM                  ")
        F_Name=input("First Name: ")
        L_Name=input("Last Name: ")
        Email=input("Email: ")
        Mobno=input("Mobile No: ")
        foundDigit=False
        while foundDigit==False: 
            if Mobno.isdigit()==False:
                print("Please provide digit only")
                Mobno=input("Mobile No: ")
            else:
                foundDigit=True
                
        city=input("City: ")
        Course=input("Course: ")
        Batch=input("Batch (Morning/Afternoon/Evening) M/A/E?: ")
        rollno=0
        with open("StudentRecords.csv","r") as stdRecords:
            for line in stdRecords.readlines():
                rollno=rollno+1
             
        print(rollno)
        stdRecords=open("StudentRecords.csv","a+")
        stdRecords.write(str(rollno)+','+F_Name+','+L_Name+','+Email+','+str(Mobno)+','+city+','+Course+','+Batch+'\n')
        stdRecords.close()
        print("Record has been successfully added.")
        continueOrExit()
'''------------------------------------------------------------------------------------------'''
def findStudent(id):
    studDetails=''
    with open("StudentRecords.csv","r") as stdRecords:  
        for record in stdRecords.readlines():
            values=record.split(',')
            if str(id)==values[0]:
                studDetails=record
    return studDetails                     
'''------------------------------------------------------------------------------------'''        
def SaveRecord(newRecord):
    print(newRecord)
    with open("StudentRecords.csv","r") as stdRecords:
        lines=stdRecords.readlines()
        startLine=0
        for line in lines:
            print(line)
            if startLine==0:
                writefile = open("StudentRecords_tmp.csv","a")
                writefile.write(line)
                writefile.close()
                startLine=1
            elif newRecord.split(',')[0]==line.split(',')[0]:
                writefile = open("StudentRecords_tmp.csv","a")
                writefile.write(newRecord)
                writefile.close()
            else:
                writefile = open("StudentRecords_tmp.csv","a")
                writefile.write(line)
                writefile.close()
    os.remove("StudentRecords.csv")
    os.rename("StudentRecords_tmp.csv","StudentRecords.csv")    
    print("Record saved successfully.")
    continueOrExit()     
    
'''-----------------------------------------------------------------------------------------'''
def DeleteRecord(id):
    with open("StudentRecords.csv","r") as stdRecords:
        lines=stdRecords.readlines()
        startLine=0
        for line in lines:
            if startLine==0:
                writefile = open("StudentRecords_tmp.csv","a")
                writefile.write(line)
                writefile.close()
                startLine=1
            elif str(id)==line.split(',')[0]:
                '''Skip thisrecord'''
            else:
                writefile = open("StudentRecords_tmp.csv","a")
                writefile.write(line)
                writefile.close() 
         
    os.remove("StudentRecords.csv") #deletes the original file
    os.rename("StudentRecords_tmp.csv","StudentRecords.csv")    
    print("Record successfully deleted.")
    continueOrExit()
'''--------------------------------------------------------------------------------------------'''
def printStudentRecord(studDetails):
    record=studDetails.split(',')
    print("RollNo : "+str(record[0]))
    print("F_Name : "+str(record[1]))
    print("L_Name : "+str(record[2]))
    print("EmailId : "+str(record[3]))
    print("MobileNo : "+str(record[4]))
    print("City : "+str(record[5]))
    print("Course : "+str(record[6]))
    print("BatchTime : "+str(record[7]))
'''--------------------------------------------------------------------------------------------'''
#Function to read students Details
def readStudentdetailsById(id):
    studDetails=findStudent(id)           
    if studDetails != '':
        printStudentRecord(studDetails)
    else:
        print("Student ID =" +str(id)+" is not present")
        
    continueOrExit()

'''----------------------------------------------------------------------------------------------'''
    
def getStudentDetails():
    print("Provide student ID to get detail")
    try:
        id=int(input())
    except:
        print("Given student id is not valid or details are not present for given ID")
        option=input("Do you want to try with different ID? Y/N")
        if option== 'Y':
            getStudentDetails()
        else:
            operationsOption()
            
    readStudentdetailsById(id)
'''-----------------------------------------------------------------------------------'''
def UpdateStudentDetail(studentDetail):
    updatedStudent=''
    line=studentDetail.split(',')
    print("RollNo : "+line[0]+"\n")
    updatedStudent=line[0]
    val=input("F_Name : "+line[1]+" Do you want to update? Y/N ")
    if 'Y'==val.upper():
        F_Name=input("Provide new value: ")
        updatedStudent+=','+F_Name
    else:
        updatedStudent +=','+line[1]

    val=input("L_Name : "+line[2]+" Do you want to update? Y/N ")
    if 'Y'==val.upper():
        L_Name=input("Provide new value: ")
        updatedStudent+=','+L_Name
    else:
        updatedStudent +=','+line[2]

    val=input("EmailId : "+line[3]+" Do you want to update? Y/N ")
    if 'Y'==val.upper():
        EmailId=input("Provide new value: ")
        updatedStudent+=','+EmailId
    else:
        updatedStudent +=','+line[3]

    val=input("MobileNo : "+line[4]+" Do you want to update? Y/N ")
    if 'Y'==val.upper():
        MobileNo=input("Provide new value: ")
        updatedStudent=str(MobileNo)
    else:
        updatedStudent +=','+line[4]

    val=input("City : "+line[5]+" Do you want to update? Y/N ")
    if 'Y'==val.upper():
        City=input("Provide new value: ")
        updatedStudent+=','+str(City)
    else:
        updatedStudent +=','+line[5]

    val=input("Course : "+line[6]+" Do you want to update? Y/N ")
    if 'Y'==val.upper():
        Course=input("Provide new value: ")
        updatedStudent+=','+str(Course)
    else:
        updatedStudent +=','+line[6]

    val=input("BatchTime : "+line[7]+" Do you want to update? Y/N ")
    if 'Y'==val.upper():
        BatchTime=input("Provide new value: ")
        updatedStudent+=','+str(BatchTime)
    else:
        updatedStudent +=','+line[7]
        
    option=input("Do you want to save it? Y/N ")
    if 'Y'==option.upper():
        return updatedStudent
    else:
        continueOrExit()
        
'''-----------------------------------------------------------------------------------'''
#function to Update Student
def updateStudent():
    print("Provide student ID to get detail")
    try:
        id=int(input()) 
    except:
        print("Given student id is not valid or details are not present for given ID")
        option=input("Do you want to try with different ID? Y/N")
        if option== 'Y':
            updateStudent()
        else:
            option=operationsOption()
            process(option)
    studDetails=findStudent(id)
    if studDetails != '':
        printStudentRecord(studDetails)
        value=input("Is it correct student details, do you wanted to update? Y/N")
        if value.upper()=='Y':
           newRecord = UpdateStudentDetail(studDetails)
           if newRecord != '':
               SaveRecord(newRecord)
        else:
           updateStudent() 
    else:
        print("Student ID =" +str(id)+" is not present")
        
    continueOrExit()   
'''-----------------------------------------------------------------------------------------'''

#funtion to Delete Student
def deleteStudent():
    print("Provide student ID to delete record")
    try:
        id=int(input())
    except:
        print("Given student id is not valid or details are not present for given ID")
        option=input("Do you want to try with different ID? Y/N")
        if option== 'Y':
            deleteStudent()
        else:
            operationsOption()
            
    studDetails=findStudent(id)
    
    if studDetails == '':
       print("Student ID =" +str(id)+" is not present")
       continueOrExit()
    else:
        print(studDetails)
        val=input("Do you want to continue? ")
        if val.upper()=='Y':
            DeleteRecord(id)
        else:
            continueOrExit()
            
         
    

'''-----------------------------------------------------------------------------------------'''

#function to Log out
def logOut():
    print("Thank you!")
    sys.exit()
'''-----------------------------------------------------------------------------------------'''

#Perform operation as per admin choice
def process(option):
    switcher={
        1:getStudentDetails,
        2:createStudent,
        3:updateStudent,
        4:deleteStudent,
        5:logOut
        }
    func=switcher.get(option,"Invalid input")
    return func()
'''-----------------------------------------------------------------------------------------'''

#First methode called  from starting point
def adminMain():
    username="USERNAME="+ input("Please enter the username: ") 
    password="PASSWORD="+input("Please enter the password: ")
    
    isUserPassCorrect=checkUserPass(username,password)

    if not isUserPassCorrect: 
        print("Please provide correct username and password")
        adminMain()
    else:
       print("Well come Admin")
       option=operationsOption()
       process(option)
'''-----------------------------------------------------------------------------------------'''

#Staring point of the application
if __name__== "__main__":
    import sys,os,csv
    print("Well come to Admission Managemnt System")
    print("Please Login as administarator")
    adminMain()
'''-----------------------------------------------------------------------------------------'''    
    
  
