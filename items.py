def itemslist():
    import random
    print(" \t\t!! ITEMS PAGE !! \n")
    fp=open("itemslist.txt")
    c=fp.read()
    cp=fp.readlines()
    print(c)
    fp.close()
    total=0
    l=[]
    l1=[]
    l2=[]
    fp=open("itemslist.txt",'r')
    cp=fp.readlines()
    while True:
        dish_no=input("\nChoose dish number-> ")
        l.append(dish_no)
        quantity=int(input("Enter Quantity->\n "))
        l1.append(quantity)
        for i in cp:
            k=i.rstrip().split(",")
            if k[0]==dish_no:
                total = total + (quantity *int(k[2]))
        ch=input("Press 'y' to choose another dish: ").lower()
        if ch=='y':
            continue
        else:
            order_no=random.randint(1,50) + random.randint(50,100) 
            print("\t\t\t\t***YOUR ORDER LIST***")
            print(f"\n\t Order number:{order_no}")
            l2.append(f"{order_no}")
            l2.append(f",")
            for i in cp:
                k=i.rstrip().split(",")
                for j in range(len(l)):
                    if k[0]==l[j]:
                        print(f"{k[1]},{l1[j]}")
                        l2.append(f"{k[1]},{l1[j]},")
            l2.append("\n")
            print("\n\t\t TOTAL AMOUNT IS :",total)
            break
    ch2=input("Enter y to confirm for the order \t\tEnter n to decline the order: ")
    if ch2=='y':
        print("\n\t\t🥳🥳 Order recieved !! Visit Again.🥳🥳 ")
        orderlist=open("orderlist.txt",'a')
        orderlist.writelines(l2)
        #orderlist.close()
    else:
        print("\n\t\t\t💓💓💓🆃🅷 🅰 🅽🅺  🆈 🅾 🆄💓💓💓")
        print("\n\t\t\t\tRelogin for our services🙏")