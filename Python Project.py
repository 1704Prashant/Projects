# import numpy as np
# import matplotlib.pyplot as plt
import random
import time
acc=[]
firstname=[]
middlename=[]
lastname=[]
mobilenum=[]
aadharcard=[]
index=-1
bankmanagerpass=["bankmanager123"]


print("\n\n\n\t\t------------  Welcome To VSB Bank  ---------------")

def details(firstname,middlename,lastname,mobilenum,aadharcard):
    
    acc_n=input("\n\t\t Enter your Account Number to see your details: ")
    print("\n\n\t")
    for i in range(0,6):
        time.sleep(1)
        print("----Loading----", end=" ")

    for i in range(len(acc)):
        if(acc_n==acc[i]):
            print("\n\n\t "+"-"*59)
            print("\t | Full Name :         || ",firstname[i],middlename[i],lastname[i]," "*(30-(len(firstname[i])+len(middlename[i])+len(lastname[i])+2)),"|")
            print("\t "+"-"*59)
            print("\t | Mobile Number :     || ","xxxxxx"+mobilenum[i][7:10]," "*(21),"|")
            print("\t "+"-"*59)
            print("\t | Aadhar Card Number :|| ","xxxx xxxx",aadharcard[i][10:14]," "*(16),"|")
            print("\t "+"-"*59)
            break;
    else:
            print("\n\nYou have entered incorrect Account Number!!!!")
            print("\nTry once more: ")
            details(firstname,middlename,lastname,mobilenum,aadharcard)
            

def check(an):
    if(an[4] == " " and an[9] == " " and an!="0000 0000 0000" and len(an) == 14 and an[0]!=0):
        print("\n\t\t( You have entered correct pattern of Aadhar Card ) ")
    else:
        print("\n Entered wrong pattern of Aadhar card ")
        print("Again Enter Correct AaDhar Card in this form(1111 1111 1111")
        an = input("\n\t\t Aadhar Card (1111 1111 1111) : ")
        check(an)
    aadharcard.append(an)

def check2(pn):
    if(len(pn)!=10 or pn=="0000000000" or pn[0]==0):
        print("You have entered wrong Phone number!!!!!!! ")
        print("Please Enter Correct Phone Number: ")
        pn1=int(input("\n\t\t Mobile Number: "))
        pn=(str(pn1))
        check2(pn)
    mobilenum.append(pn)

def checknamesfn(fn):
    cl={"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,"K":11,"L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26}
    for i in cl:
        if(i==fn[0].upper()):
            firstname.append(fn)
            break
    else:
        print("!!!!Please enter the first letter of names in Alphabet!!!!")
        fn=input("\n\n\t\t First Name: ")
        checknamesfn(fn)
        
def checknamesmn(mn):
    cl={"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,"K":11,"L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26}
    for i in cl:
        if(i==mn[0].upper()):
            middlename.append(mn)
            break
    else:
        print("Please enter the first letter of names in Alphabet!!!!")
        mn=input("\n\t\t Middle Name ( Father Name ): ")
        checknamesmn(mn)

def checknamesln(ln):
    cl={"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,"K":11,"L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26}
    for i in cl:
        if(i==ln[0].upper()):
            lastname.append(ln)
            break
    else:
        print("\n\t\t\t(Please enter the first letter of names in Alphabet!!!!)")
        ln=input("\n\t\t Last Name: ")
        checknamesln(ln)

def allacounts():
    for i in range(len(acc)):
            print("\n")
            print("\n\t "+"-"*59)
            print("\t | Full Name :         || ",firstname[i],middlename[i],lastname[i]," "*(30-(len(firstname[i])+len(middlename[i])+len(lastname[i])+2)),"|")
            print("\t "+"-"*59)
            print("\t | Mobile Number :     || ",mobilenum[i]," "*(21),"|")
            print("\t "+"-"*59)
            print("\t | Aadhar Card Number :|| ",aadharcard[i]," "*(16),"|")
            print("\t "+"-"*59)
            print("\t | Account Number :    || ",acc[i]," "*(19),"|")

def bankmanager(admin):
    if(admin=="1"):
        if(acc!=[]):
            allacounts()
            time.sleep(5)
            admin=input("\n\n\t 1. All Account Details \n\t 2. Password Change \n\t 3. Back to the main page \n\t 0. Exit \n\n\t Choose your choice :  ")
            bankmanager(admin)

        else:
            print("\n\n\tThere is No Account Added Yet!!!!!")
            time.sleep(2)
            admin=input("\n\n\t 1. All Account Details \n\t 2. Password Change \n\t 3. Back to the main page \n\t 0. Exit \n\n\t Choose your choice :  ")
            bankmanager(admin)
    elif(admin=="2"):
        countold=0
        oldpass=input("Enter your old password: ")
        if(oldpass != bankmanagerpass[-1]):
            print("Incorrect Old Password")
            countold+=1
            admin=input("\n\n\t 1. All Account Details \n\t 2. Password Change \n\t 3. Back to the main page \n\t 0. Exit \n\n\t Choose your choice :  ")
            bankmanager(admin)  
            if(countold==3):
                print("!!!!!!  I think you have forgotten your password  !!!!!! ")
                print(" \n\t\tHAVE A Good DAY Buddy")
                print(" \n\t\tTHANK YOU FOR VISITING OUR BANK   ")
                exit() 
        newpass=input("Enter the new password : ")
        bankmanagerpass.append(newpass)
        print("----Successfully your password has been changed----")
        time.sleep(3)
        admin=input("\n\n\t 1. All Account Details \n\t 2. Password Change \n\t 3. Back to the main page \n\t 0. Exit \n\n\t Choose your choice :  ")
        bankmanager(admin) 
    elif(admin=="3"):
        b = input("\n\n\t 1. Open a new Account \n\t 2. Check Your Existing Account Details \n\t 3. Bank Manager \n\t 0. Exit the bank \n\n\t Choose the above option : \t ")
        Account(b)
    elif(admin=="0"):
        print(" \n\t\t\tHAVE A NICE DAY ")
        print(" \n\t\t----THANK YOU FOR VISITING OUR BANK----")
        exit()


    else:
        print("\n\tEntered wrong choice!!!!!")
        time.sleep(2)
        admin=input("\n\n\t 1. All Account Details \n\t 2. Password Change \n\t 3. Back to the main page \n\t 0. Exit \n\n\t Choose your choice :  ")
        bankmanager(admin)

def Account(b):
    if(b =="1"):
        global index
        print(" \n\tLet's make a new Account: ")
        fn=input("\n\n\t\t First Name: ")
        checknamesfn(fn)
        mn=input("\n\t\t Middle Name ( Father Name ): ")
        checknamesmn(mn)
        ln=input("\n\t\t Last Name: ")
        checknamesln(ln)
        while True:
            try:
                pn1=int(input("\n\t\t Mobile Number: "))
                break
            except ValueError:
                print(" It was not a valid number")
        pn=(str(pn1))
        check2(pn)
        
        an=input("\n\t\t Aadhar Card (1111 1111 1111) : ")
        check(an)
        index+=1
        first=fn[0].upper()
        cl={"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,"K":11,"L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26}
        if cl[first]>=10:
            acc3="456"+str(random.randint(11,99))+str(cl[first])+pn[0:2]+an[0:2]
            acc.append(acc3)
        else:
            acc3="456"+str(random.randint(11,99))+"0"+str(cl[first])+pn[0:2]+an[0:2] 
            acc.append(acc3)  
        # print(acc)
        time.sleep(5)
        print("\n\t\t------ Your Account Number is Generated ------ : ",acc[index])
        time.sleep(3)

        b = input("\n\n\t 1. Open a new Account \n\t 2. Check Your Existing Account Details \n\t 3. Bank Manager \n\t 0. Exit the bank \n\n\t Choose the above option : \t ")
        Account(b)
 
    elif(b=="2"):
        # for i in range(len(acc)):
        count=0
        if acc!=[]:
            re=input("\n\n\t\tWanted to check your Added Account Details (Y or N) ")
            if(re=="Y" or re=="y"):
                details(firstname,middlename,lastname,mobilenum,aadharcard)
                time.sleep(3)
                b = input("\n\n\t 1. Open a new Account \n\t 2. Check Your Existing Account Details \n\t 3. Bank Manager \n\t 0. Exit the bank \n\n\t Choose the above option : \t ")
                
                Account(b)
            elif(re=="N" or re=="n"):
                b = input("\n\n\t 1. Open a new Account \n\t 2. Check Your Existing Account Details \n\t 3. Bank Manager \n\t 0. Exit the bank \n\n\t Choose the above option : \t ")
                Account(b)
                
            else:
                count+=1
                print("\nEntered Wrong Input !!!!!")
                b = input("\n\n\t 1. Open a new Account \n\t 2. Check Your Existing Account Details \n\t 3. Bank Manager \n\t 0. Exit the bank \n\n\t Choose the above option : \t ")
                Account(b)
                
                if(count==3):
                    print("!!!!!!  You are not Capable to Read the Instructions  !!!!!! ")
                    print(" \n\t\tHAVE A Good DAY Buddy")
                    print(" \n\t\tTHANK YOU FOR VISITING OUR BANK   ")
                    exit()
        else:
            print("\n\n\tThere is No Account Added Yet!!!!!")
            time.sleep(2)
            b = input("\n\n\t 1. Open a new Account \n\t 2. Check Your Existing Account Details \n\t 3. Bank Manager \n\t 0. Exit the bank \n\n\t Choose the above option : \t ")
            Account(b) 
    elif (b=="3"):
            print("\n\n\t******  WELCOME SIR  *******")   
            bm=input(" \nFirst Enter the password , Sir  :  ")
            countpass=0
            bankmanagerpass[-1]
            if(bm==bankmanagerpass[-1]):
                print("\n\n\t---- Successfully you are logged in your account ----\n")
                admin=input("\n\n\t 1. All Account Details \n\t 2. Password Change \n\t 3. Back to the main page \n\t 0. Exit \n\n\t Choose your choice :  ")
                bankmanager(admin)
            else:
                countpass+=1
                print("\nEntered Wrong Password !!!!!")
                if(countpass==4):
                    print("!!!!!!  You are not Capable to Read the Instructions  !!!!!! ")
                    print(" \n\t\tHAVE A Good DAY Buddy")
                    print(" \n\t\tTHANK YOU FOR VISITING OUR BANK   ")
                    exit()
                b = input("\n\n\t 1. Open a new Account \n\t 2. Check Your Existing Account Details \n\t 3. Bank Manager \n\t 0. Exit the bank \n\n\t Choose the above option : \t ")
                Account(b)

    elif(b=="0"):
        print(" \n\t\t\tHAVE A NICE DAY ")
        print(" \n\t\t----THANK YOU FOR VISITING OUR BANK----")
        exit()
    else:
        print("\n\tEntered wrong choice!!!!!")
        time.sleep(2)
        b = input("\n\n\t 1. Open a new Account \n\t 2. Check Your Existing Account Details \n\t 3. Bank Manager \n\t 0. Exit the bank \n\n\t Choose the above option : \t ")
        Account(b)
    
b = input("\n\n\t 1. Open a new Account \n\t 2. Check Your Existing Account Details \n\t 3. Bank Manager \n\t 0. Exit the bank \n\n\t Choose the above option : \t ")
Account(b)

