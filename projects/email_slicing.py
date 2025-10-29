while True:
    email=input("enter your Email: ").lower()
    if "@" not in email:
        print("invalid email..!try again")
        continue
    else:
        user_name=email[:email.index("@")]
        domain=email[email.index("@")+1:]
        print(f"your username is {user_name} for {domain}")
        user_exit=input("you want to exit? (y/n)").lower()
        if user_exit=="y":
            print('Done...you are exiting')
            break