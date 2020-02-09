def create_account():
    email = input("Enter your email\n")
    password = input("Enter your password")
    if email in Email:
        print("There is an existing account with this email")
        transaction()
    else:
        Email.append(email)
        print("Account successfully created")
def transaction():
    email = input("Enter your email\n")
    password = input("Enter your password")
    if email not in Email:
        create_account()
        
response = print(input("Enter an option\n 1.Create account\n 2.Transaction\n"))
Email = ['Odumije@gmail.com','Ebenezer@gmail.com']
if response == "1":
    create_account()
elif response == "2":
    transaction()
else:
    print("response not in range")
