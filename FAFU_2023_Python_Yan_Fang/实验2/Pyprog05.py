dic1={"Jane":"abc","Mike":"123","Marry":"123456","Rose":"abc123","Tom":"123456"}

user=input()

key=input()
if(user in dic1):
    if(dic1[user]==key):

        print("Successful login")

    elif(dic1[user]!=key):

        print("The password is incorrect")

else:

    print("The user does not exist")

