def work():
    fp = open("itemslist.txt",'r')
    cp=fp.readlines()
    l=[]
    for i in cp:
        k=i.strip().split(",")
        l.append(k[0])
        print("1--->add a new item \n2--->delete a item \n3--->update the price of item \n")
        ch1= input("Enter choice:")
        if ch1=='1':
            item_no=input("Enter item no: ")
            if item_no in l:
                print("\t\t\t\t---Item already exists---")
            else:
                item_name=input("Enter item name: ")
                price=input("Enter item price: ")
                fp=open("itemslist.txt","a")
                fp.writelines(item_no + " , " + item_name +" , " + price + '\n')
                print("\t\t\t\tItem added successfully!!\n")
        elif ch1=='2':
            fp=open("itemslist.txt","r+")
            c=fp.readlines()
            fp.seek(0)
            ch2=input("Enter item number to be deleted: ")
            if ch2 in l:
                for i in c:
                    k=i.strip().split(",")
                    if k[0]!=ch2:
                        fp.write(i)
                fp.truncate()
                print("\t\t\t\tItem deleted")
            else:
                print("item not present")
        elif ch1=='3':
            fp=open("itemslist.txt",'r')
            cp=fp.readlines()
            item_no=input("Enter item no.")
            if item_no in l:
                name=input("Enter item name:")
                price=input("enter the price to be updated: ")
                if price.isdigit():
                    for i in range(len(cp)):
                        if name in cp[i]:
                            cp[i] = item_no + "," +name+" , "+price+"\n"
                            print(cp[i])
                            print("\t\t\t\t---UPDATED---")
                            flag = 1                            
                            break
                    if flag == 0:
                        print("not found")
                else:
                    print("Price contains only Digits")
                
                fp=open("itemslist.txt",'w')
                cp=fp.writelines(cp)
            else:
                print("Item not found")
        
    else:
        print("I\t\t\tnvalid Choice!!!")
                
            
                
             