import items
fp=open("customer.txt")
details=fp.read()
fp.close()
def login():
    print("\t\t\t\t\t\t----Customer Page-----")
    print("\t\t\t\t      1. Sign up  \t\t\t2. Sign in")
    ch=int(input("enter 1 if you are a new user or 2 if you are an existing user: "))   
    if ch==1:
        while True:
            name=input("Enter your name: ")
            if name in details:
                print("try another user name!!")
                continue
            else:
                break
        
        while True:
            password=input("Enter your password: ")
            special=["@","#","$","%","!","/","?"]
            if len(password)<6:
                print("at least 6 characters required")
                continue
            elif not any (char.isdigit() for char in password):
                print("at least one digit")
                continue
            elif not any (char.isupper() for char in password):
                print("at least one capital letter")
                continue
            elif not any(char.islower() for char in password):
                print("at least one small letter")
                continue
            elif not any(char in special for char in password):
                print("at least one special character")
                continue
            else:
                print("\t\t\t\t🙏🙏Log-in successful🙏🙏\n")
                break
        fp=open("customer.txt","a")
        content=name+","+password+"\n"
        fp.write(content)
        fp.close()
        items.itemslist()
    elif ch==2:
        while True:
            name=input("Enter your Name: ")
            if name in details:
                password=input("Enter your Password: ")
                if password in details:
                    print("\t\t\t\t\t🙏🙏Logged-in Successfully🙏🙏\n")
                    break
                else:
                    print("Password is Invalid!!!!")
                    continue
                
            else:
                print("your name is not in our data!!")
                print("please try again")
                continue
        items.itemslist()         
    else:
        print("invalid option")