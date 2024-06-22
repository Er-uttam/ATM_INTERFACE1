print("---ATM INTERFACE---\n")
print("Insert Your Card!")
print("Select Language : (English,Nepali) \n")


pin = int(input("Enter Your Pin : "))
if pin==1234:
 balance = 0 
     
 while True:

   print("-------------------")
   print("1. Withdraw")
   print("2. Deposit Amount.")
   print("3. Check Balance.")
   print("4. Exit.")
   print("-------------------\n")
  
   
   
   choice = int(input("Enter Your Option:"))

   match choice:
      
       case 1:
           amount = float(input("Enter Amount to withdraw:"))
           if amount > balance:
              print("Insufficient Balance.")
           elif amount <= 0:
              print("Withdraw amount must be positive.")
           else:
              balance -= amount
              print(f"{amount} has been withdraw from your account.")
              
       case 2:
           amount = float(input("Enter Amount to deposit:"))
           if amount>0:
              balance += amount
              print(f"{amount} has been deposited to your account.")
           else:
              print("Deposit amount must be positive.")
   
       case 3:
           print(f"Your Balance  is: {balance}")
       case 4:
          print("Exiting ATM interface. Thank you!")
          break
       case _:
            print("Invalid choice. Please try again.")
else:
    print("Incorrect Pin!")

