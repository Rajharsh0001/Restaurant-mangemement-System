import user
import owner
print("=="*76)
print("\n\n\t\t\t\t\t\t😎😎😎😎😎🙏WELCOME to our RESTAURANT🙏😎😎😎😎😎\n\n")
print("=="*76)
print("-->Please choose the choices as directed-->")
print("1--> Customer\n2-->Owner\n")
ch=int(input("Enter your choice 1 or 2: "))
if ch==1:
    user.login()
elif ch==2:
    owner.login()
else:
    print("Sorry!! invalid choice")