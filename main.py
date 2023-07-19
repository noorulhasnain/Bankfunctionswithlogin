
  





def getDepositAmount():
  #handles getting the amount the user wants to deposit 
  while True:
     time.sleep(2)
     os.system('clear')
     try:
        
        depositAmount=float(input("how much money would you like to deposit :"))
  
     except:#makes sure that the program doesn't crash if a string is inputted 
  
          os.system('clear')
          depositAmount=0
          print("invalid input enter a number")
          time.sleep(2)
          os.system('clear')
          continue
      
       #input is made float due it being able to handle decimals and whole numbers 
     time.sleep(2)
     os.system('clear')
  
  
    
     if depositAmount<1:#makes sure that negative numbers are not inputted 
        print("negative numbers not allowed")
        time.sleep(2)
        os.system('clear')
        os.system('clear')
        depositAmount=0
        print("negative numbers not allowed")
        continue
        time.sleep(1)
        os.system('clear')
        continue
        os.system('clear')
       
     return depositAmount
 
 
def deposit(accountBalance, depositAmount):
  accountBalance+=depositAmount
  #actually deposits the money the user specfied  

  return accountBalance 
  
 
def getWithdrawalAmount(accountBalance):
  #handles getting the withdrawl amount from the user 
 while True:
  try: 
     os.system('clear')
     WithdrawlAmount=float(input("how much money would you like to withdraw :"))
     time.sleep(2)
     os.system('clear')

     if WithdrawlAmount>accountBalance:#makes sure the withdrawl amount isn't larger than the money the user has 
        WithdrawlAmount=0
        print("you have too little money to widthraw that much money")
        time.sleep(2)
        os.system('clear')
        continue 

     elif WithdrawlAmount<1:#makes sure negative numbers aren't inputted 
       
         WithdrawlAmount=0
         print("\n  negative numbers not allowed ")
         continue
  except: #makes sure the program isn't crashed by a string  
    os.system('clear')
    WithdrawlAmount=0
    print("invalid input enter a number")
    time.sleep(2)
    os.system('clear')
    continue
    
    
  return WithdrawlAmount

 
def withdraw(withdrawlAmount, accountBalance):
 #actually withdrawls the money from the user 
  accountBalance-=withdrawlAmount
  
 
  return accountBalance
 
 
def printBalance(accountBalance):
  #prints out the user's balance 

 os.system('clear')
 print("********************************")
 print(("you have "+str(accountBalance)+" dollars"))
 print("********************************")
 time.sleep(2)
 os.system('clear')






import time 
import os 

def listOfLinesGenerator():
  with open('acounts.txt','r')as f:
     linesList=f.readlines()
     return linesList
  
  pass #this function will read the file and return a list of all the lines
def removeAllNewlineCharaters(linesList):  
  for i in range(len(linesList)):
    linesList[i] = linesList[i].strip('\n') #Removes \n from the end of each elemtnt
  return linesList

def usernameListGenerator(linesList):
  usernameList=[]
  for i in linesList:
    tempList=[]
    
    tempList=i.split(" ")
    usernameList.append(tempList[0])
 

  return usernameList #creates  the list of all usernames which is critical in this program's ability to function 

def passwordListGenerator(linesList):
  passwordlist=[]
  for i in   linesList:
    tempList=[]
   
    tempList=i.split(" ")
    passwordlist.append(tempList[1])
  
    
  return passwordlist #return the list of all passwords

def accountBalanceListGenerator(linesList):
  accountBalanceList=[]
  for i in linesList:
    tempList=[]
    
    tempList=i.split(" ")
    accountBalanceList.append(tempList[2])
    for i in range(len(accountBalanceList)):
      accountBalanceList[i] = accountBalanceList[i].strip('\n')# removes \n from the end of all elements 
  return accountBalanceList  #return the list of all account balances


def rewriteFile(usernameList, passwordList, accountBalanceList):
  #when the user's accountbalance is changed we need to rewrite the file this function handles that 
  with open("acounts.txt",'w') as file:
    for i in range (len(usernameList)):
      line= str(usernameList[i])+" "+str(passwordList[i])+" "+str(accountBalanceList[i])+"\n"
      file.write(line)

def createAccount(usernameList):#this function handles the creation of a account if the user specefies that they would like to create one 
    with open('acounts.txt','a')as f:
      while True:
        userName=str(input("enter the username you would like to create :"))
        if userName in usernameList:
          print(userName+" is already taken\n\n")#makes sure that the user cannot take a username that has already been selected 
          time.sleep(1)
          os.system('clear')
          continue
  
        else:
          password = input("enter the password you would like to create :")
          break
      while True:
        try:
                accountBalance=int(input("how much money would  you like to start with :"))
                if accountBalance<0:#makes sure the account balance the user specifies isn't less then 0 
                  os.system('clear')
                  print("\n\n\n no negative numbers")
                  time.sleep(1)
                  
                  os.system('clear')
                  continue 
                  
                  
                else:
                  break
                  break
        except:#makes sure that a string being inputted will not crash the program 
                print("\n\n\n invalid input enter a number")
                time.sleep(2)
                os.system('clear')
                continue 
      f.write(userName+" "+password+" "+str(accountBalance)+"\n")#adds the new account into the file 
   


  
def login():
  #handles the login and makes sure that the user is entering a username and password that exists 
  attempts=0
  while attempts<3:

    
    username=input("enter your username :")
    password=input("enter your password :")
    attempts+=1
  
    index=usernameListGenerator(listOfLinesGenerator()).index(username)
    accountBalance=accountBalanceListGenerator(listOfLinesGenerator())[index]
    
    if username in usernameListGenerator(listOfLinesGenerator())== False:
      print("The username doesn't exist") 
      continue 

    if passwordListGenerator(listOfLinesGenerator())[index]==password:
        print("you're logged in ")
        return index 
    else:
     print("wrong information")
     continue
  print("you have used all your tries ")
    

  #handless login
# login()
while True:
  #this is the main loop that logs into the users account and calls the function that handles the login and create account process 
 try:
    userChoice=int(   input(" welcome to noor bank\n (1)  make an account\n (2)  log in \n"))
    if userChoice==1:#calls the function that handles account creation 
      os.system("clear")
      createAccount(usernameListGenerator(listOfLinesGenerator()))
      time.sleep(2)
      os.system('clear')
      
    elif userChoice==2:#calls the fuction that handles login 
        os.system('clear')
        listOfLinesGenerator()
        index=login()
        time.sleep(1)
        os.system('clear')
        
        passwordList = passwordListGenerator(listOfLinesGenerator())
        usernameList = usernameListGenerator(listOfLinesGenerator())
        accountBalanceList = accountBalanceListGenerator(listOfLinesGenerator())
        accountBalance=float(accountBalanceList[index])
        while True: 
         try:
           userChoice = int(input('Welcome to noor bank. Please pick one of the following options....\n1. Deposit\n2. Withdrawal\n3. Account balance\n4. Exit bank\nEnter your choice [1,2,3,4]:'))
         except:
           os.system('clear')
           time.sleep(0.5)
           print("invalid input make sure to enter a number ")
           time.sleep(2)
           os.system("clear")
           continue
         if userChoice==1:#calls the function handaling deposit 
          
           accountBalance = deposit(accountBalance, getDepositAmount())
           accountBalanceList[index] = accountBalance
           rewriteFile(usernameList, passwordList,accountBalanceList)
           
         elif userChoice==2:#calls the funcion handiling withdrawl 

  
                                 accountBalance=withdraw(getWithdrawalAmount(accountBalance),accountBalance)
                                 accountBalanceList[index] = accountBalance
                                 rewriteFile(usernameList, passwordList,accountBalanceList) 
  
         elif userChoice==3:#prints out the balalnce of the user's account 
           printBalance(accountBalance)
         elif userChoice==4:#logs out of the bank and goes back to the title screen 
          time.sleep(1)
          os.system('clear')
          print("logged out")
          time.sleep(0.5)
          os.system('clear')
          break
         else:#makes sure that invalid inputs return the program to the title screen 
          os.system('clear')
          print("not a valid input")
          time.sleep(2)
          os.system('clear')
        

 except:#makes sure that when strings are entered the program doesn't crash 
    print("invalid input")
    time.sleep(1)
    os.system('clear')

        