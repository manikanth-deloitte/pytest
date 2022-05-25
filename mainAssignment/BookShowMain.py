from adminActions import adminAction
from userRegister import user_register
from user import userlogin


def welcome():
    print("******Welcome to BookMyShow*******\n1.Login\n2.Register\n3.Exit")


def option():
    option = int(input("enter option: "))
    return option


def main():
    admin_dic = {
        'pass': 'admin123'
    }
    while True:
        welcome()
        opt = option()

        if opt == 1:
            print("******Welcome to BookMyShow*******")
            user = input("enter login id: ")
            password = input("enter password:")
            if user == 'Admin':
                if admin_dic['pass'] == password:
                    adminAction()
            else:
                print("******Welcome to BookMyShow******* ")
                userlogin(user, password)

        elif opt == 2:
            print("****Create new Account***** ")
            user_register()
        else:
            print("Thank you!")
            break


if __name__ == "__main__":
    main()