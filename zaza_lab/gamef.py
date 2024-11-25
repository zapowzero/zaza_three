print("""
███╗   ███╗ ██████╗ ███╗   ██╗███████╗████████╗███████╗██████╗     ███████╗██╗      █████╗ ██╗   ██╗███████╗██████╗ 
████╗ ████║██╔═══██╗████╗  ██║██╔════╝╚══██╔══╝██╔════╝██╔══██╗    ██╔════╝██║     ██╔══██╗╚██╗ ██╔╝██╔════╝██╔══██╗
██╔████╔██║██║   ██║██╔██╗ ██║███████╗   ██║   █████╗  ██████╔╝    ███████╗██║     ███████║ ╚████╔╝ █████╗  ██████╔╝
██║╚██╔╝██║██║   ██║██║╚██╗██║╚════██║   ██║   ██╔══╝  ██╔══██╗    ╚════██║██║     ██╔══██║  ╚██╔╝  ██╔══╝  ██╔══██╗
██║ ╚═╝ ██║╚██████╔╝██║ ╚████║███████║   ██║   ███████╗██║  ██║    ███████║███████╗██║  ██║   ██║   ███████╗██║  ██║
""")

users = {}

def register():
        username = input("Enter username : ")
        password = input("Enter password: ")

        users[username] = password
        print("We received your registration !")
        print("Now you are a Monster Slayer :)")

def login():
    username = input("Enter your username: ")
    if username not in users:
        print("Username not found, Please register first.")
        return False

    password = input("Enter your password: ")
    if users[username] == password:
        print(f"Hi {username}, Welcome to Monster Slayer.")
        return True
    else:
        print("Invalid password, Please try again.")
        return False

def main():
    while True:
        
        print("1 Register")
        print("2 Login")
        print("3 Exit")

        choice = input("1 or 2 or 3 : ")
        
        if choice == "1":
            register()
        elif choice == "2":
            if login():
                print("You are login now.")
                break  
        elif choice == "3":
            print("Exit")
            break
        else:
            print("Invalid, Please select again.")


if __name__ == "__main__":
    main()

