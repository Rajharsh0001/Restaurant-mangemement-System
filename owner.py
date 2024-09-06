import owner2
def login():
    print("\t\t\t\t******OWNER******")
    password=input("Enter your password: ")
    if password=="Owner@123":
        print("\t\t\t\t!!Logged in successfully!!\n")
        print("What do you want to do ????")
        while(True):
            ch=int(input("Choose 1 to Update the items list\n2 to Dispatch the live orders\n3 to View the item list \n4 to Close\n"))
            if ch==1:                
                owner2.work()
            elif ch==2:
                fp=open("orderlist.txt","r")
                c=fp.readlines()                
                print("The Live Order List is👉👉 ")
                for i in c:
                    print(i)
                fp1=open("orderlist.txt","r+")
                cp=fp1.readlines()
                fp1.seek(0)
                l1=[]
                for i in cp:
                    k1=i.rstrip().split(",")
                    l1.append(k1[0])
                    choice=input("Enter order number to dispatch👉👉 ")
                    if choice in l1:
                        for i in cp:
                            k1=i.rstrip().split(",")
                            if k1[0]!=choice:                            
                                fp1.write(i)
                        fp1.truncate()                            
                        print("Order is Dispatched")
                    else:
                        print("Order Number not Present")              
                
            elif ch==3:
                fp=open("itemslist.txt")
                print(fp.read())
                
            elif ch==4:
                print("You have choosen Exit 🥺")
                print("\n\t\t\t💓💓💓🆃🅷 🅰 🅽🅺  🆈 🅾 🆄💓💓💓")
                break
    else:
        print("SORRY!! wrong password")
        
        