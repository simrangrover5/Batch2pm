
print("*"*30,"Bank Application","*"*30)
username = "admin123"
password = "adminadmin"

while True:
    print("\n1.\tLogin\n2.\tSignup\n3.\tAdmin Login\n4.\tExit")
    ch = int(input('\nEnter your choice among them(1-3) : '))
    if ch==1:
        accno = int(input("\nEnter your account number : "))
        password = input("\nEnter your password : ")
        if accno in data['accno']:
            i = data['accno'].index(accno)
            if password == data['password'][i]:
                while True:
                    print("\n1.\tCredit\n2.\tDebit\n3.\tCheck Balanace\n4.\tUpdate Password5.\tExit")
                    ch1 = int(input("\nEnter your choice from (1-5): "))
                    if ch1==1:
                        pass
                    elif ch==2:
                        pass
                        
                    elif ch==3:
                        pass
                    elif ch==4:
                        pass
                    elif ch==5:
                        print("\n","*"*30,"Exiting....","*"*30)
                        break
                    else:
                        print("\n Invalid choice.....")

            else:
                print("\nIncorrect password.....")
        else:
            print("\nInvaid Account number.....please check it again....")
    elif ch==2:
        name = input("\nEnter your name : ")
        bal = int(input("\nEnter your balance : "))
        password = input("\nEnter your password : ")
        data['name'].append(name)
        data['bal'].append(bal)
        data['password'].append(password)
        last = len(data['accno'])-1
        newaccno = data['accno'][last] + 1
        data['accno'].append(newaccno)
        print("\nYour account number is : ",newaccno)
    elif ch==3:
        uname = input("\nEnter your username : ")
        pswd = input("\nEnter your password : ")
        if username == uname and password == pswd:
            pass
        else:
            print("\nIncorrect Information")

    elif ch==4:
        print("\n\nBye bye")
        break
    else:
        print("Invalid choice")
