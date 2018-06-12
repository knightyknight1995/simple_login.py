user1 = "myname"
passw1 = "mypass"
user = input("USERNAME: ")
if user == user1:
    passw = input("PASSWORD: ")
    if passw == passw1:
        print ("It Works")
    else:
        print ("Incorrect Password")
else:
    print ("Incorrect Username")
